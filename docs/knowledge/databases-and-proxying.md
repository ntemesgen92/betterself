# Databases & Connection Proxying - Knowledge Base

Personal reference notes from the BetterSelf database architecture decision. Covers the options we evaluated, why connection pooling matters for Lambda, and how proxying works.

*Our final decision: RDS PostgreSQL (free tier) + RDS Proxy. See [milestone_11_database.plan.md](../design/milestones/milestone_11_database.plan.md) for implementation details.*

---

## The Problem We're Solving

We have a Python FastAPI backend running on AWS Lambda. Lambda is **serverless** -- each request might spin up a new isolated container. We need a database that:

1. Stores relational data (users, calendar events, tasks, habits, conversations)
2. Supports JOINs and aggregations (needed for analytics, social features)
3. Works well with Lambda's ephemeral, concurrent execution model
4. Stays cheap during MVP (2 devs, minimal traffic)

The challenge: **SQL databases and Lambda don't play nicely together** without help. This doc explains why and how we solved it.

---

## SQL vs NoSQL: The Two Database Families

### SQL (Relational) -- e.g., PostgreSQL, MySQL, Aurora

Data is stored in **tables with fixed schemas** and linked by **foreign keys**. You query with SQL.

```sql
-- "Show me all focus sessions longer than 30 minutes this week, grouped by day"
SELECT
    DATE(start_time) AS day,
    COUNT(*) AS sessions,
    AVG(duration_seconds) / 60 AS avg_minutes
FROM blocking_sessions
WHERE user_id = 'abc-123'
  AND start_time > NOW() - INTERVAL '7 days'
  AND duration_seconds > 1800
GROUP BY DATE(start_time)
ORDER BY day;
```

**Strengths:** JOINs across tables, aggregations (AVG, SUM, GROUP BY), foreign key enforcement, ACID transactions, full-text search, mature tooling (pgAdmin, SQLAlchemy, Alembic).

**Weaknesses:** Requires persistent connections (problematic for Lambda), fixed schema means migrations for changes, scaling writes is harder than NoSQL.

### NoSQL (Non-Relational) -- e.g., DynamoDB, MongoDB

Data is stored as **key-value pairs or documents**. No JOINs, no fixed schema.

```python
# DynamoDB: get all sessions for a user
response = table.query(
    KeyConditionExpression=Key('user_id').eq('abc-123') & Key('start_time').gt('2026-03-01')
)
```

**Strengths:** Scales horizontally to millions of requests/second, no connection management (HTTP API), flexible schema, pay-per-request pricing.

**Weaknesses:** No JOINs (you query one table at a time), aggregations must be done in application code, no foreign keys (data integrity is your responsibility), querying requires knowing your access patterns upfront (GSIs).

---

## The Options We Evaluated

### Option 1: DynamoDB Only

Put everything in DynamoDB (NoSQL). Every table has a partition key (user_id) and optional sort key.

```
┌──────────┐     HTTPS      ┌───────────┐
│  Lambda  │ ──────────────→ │ DynamoDB  │
└──────────┘   (stateless)   └───────────┘

No connections. No pooling. No proxy. Simple.
```

| Aspect | Details |
|--------|---------|
| Cost | ~$0-10/month (on-demand, pay per read/write) |
| Connection management | None needed -- DynamoDB uses HTTP API |
| Setup complexity | Low -- just create tables and GSIs |

**Why we didn't choose this:**
- Calendar recurrence (RRULE with exceptions) is inherently relational
- Analytics queries ("average focus time by day of week") require scanning all records and aggregating in code
- Social features (post-MVP leaderboards, accountability groups) need many-to-many relationships
- Full-text search on conversations requires an additional service (OpenSearch)
- We'd have to migrate to SQL later when these features ship, and migrations are painful

### Option 2: Aurora Serverless v2

AWS's enhanced PostgreSQL-compatible engine with auto-scaling compute and a **Data API** (more on this below).

| Aspect | Details |
|--------|---------|
| Cost | ~$43/month minimum (0.5 ACU × $0.12/hr × 730hrs) |
| Connection management | **Data API eliminates the problem** (see below) |
| Setup complexity | Medium -- CDK stack, Secrets Manager |

**Why we didn't choose this:** The $43/month cost floor is too high for an MVP with near-zero traffic. We'd be paying $43/month for a database that handles 10 requests/day.

### Option 3: RDS PostgreSQL + Self-Hosted PgBouncer on EC2

Standard PostgreSQL on a managed instance, with an open-source connection pooler (PgBouncer) running on a small EC2 instance.

| Aspect | Details |
|--------|---------|
| Cost | RDS free tier ($0) + EC2 t4g.nano (~$3/month) = ~$3/month |
| Connection management | PgBouncer handles it |
| Setup complexity | High -- manage EC2 instance, install PgBouncer, configure TLS, monitor for crashes |

**Why we didn't choose this:** $12/month savings over RDS Proxy isn't worth the operational overhead of managing an EC2 instance (patching, monitoring, no HA, single point of failure).

### Option 4: RDS PostgreSQL + RDS Proxy (Our Choice)

Standard PostgreSQL on a managed instance, with AWS's managed connection pooler.

```
┌──────────┐   TCP 5432    ┌───────────┐   TCP 5432    ┌──────────────┐
│  Lambda  │ ────────────→ │ RDS Proxy │ ────────────→ │ RDS Postgres │
└──────────┘   (pooled)    └───────────┘   (real conn)  └──────────────┘
```

| Aspect | Details |
|--------|---------|
| Cost | RDS free tier ($0 for 12 months) + RDS Proxy (~$15/month) = **~$15/month** |
| Connection management | RDS Proxy handles it (managed, multi-AZ, auto-failover) |
| Setup complexity | Medium -- CDK stack, Secrets Manager, security groups |

**Why we chose this:** Best balance of cost, simplicity, and future-proofing. Free tier covers the MVP period. Standard PostgreSQL means full ecosystem support (SQLAlchemy, Alembic, pgAdmin). RDS Proxy is set-and-forget. No migration needed when we add analytics/social features.

---

## Connection Pooling: The Core Problem

### Why Lambda + SQL Databases Clash

A traditional server (EC2, ECS) opens a few database connections at startup and reuses them for every request:

```
Traditional Server:
┌──────────────┐     5 persistent connections     ┌──────────┐
│   Server     │ ──────────────────────────────── │ Database │
│ (1 instance) │     (reused for all requests)    │ (max 100)│
└──────────────┘                                   └──────────┘

1,000 requests/second → all share 5 connections. Database is fine.
```

Lambda is different. Each concurrent invocation runs in its own isolated container with its own memory space. Containers cannot share connections:

```
Lambda WITHOUT proxy:
┌─ Lambda 1 ─┐
┌─ Lambda 2 ─┐     1 connection each     ┌──────────┐
┌─ Lambda 3 ─┐  ────────────────────────  │ Database │
│     ...     │                            │ (max 100)│
┌─ Lambda 200─┐                            └──────────┘

200 concurrent requests → 200 connections.
PostgreSQL default max is ~100.
Connection 101 gets: "FATAL: too many connections for role"
```

It gets worse: Lambda containers stay alive for 5-15 minutes after handling a request (AWS keeps them warm for potential reuse). During that time, each holds its database connection open. So connections pile up even when traffic is low.

### What a Connection Is (Under the Hood)

A database connection is a **persistent TCP socket** between your application and PostgreSQL:

```
1. TCP 3-way handshake (SYN → SYN-ACK → ACK)           ~1-5ms
2. TLS handshake (if encrypted)                          ~5-20ms
3. PostgreSQL authentication (username/password/IAM)      ~5-10ms
4. PostgreSQL allocates memory for the session            ~10MB
5. Connection is now "open" -- can send SQL queries

Total setup time: ~10-35ms
Memory cost: ~10MB per connection on the database server
```

This setup cost is why connections are reused (pooled) rather than opened/closed per query.

---

## How RDS Proxy Solves This

RDS Proxy is a **managed middleman** that sits between Lambda and the database. It maintains a pool of real database connections and lends them to Lambda instances on demand:

```
Lambda WITH RDS Proxy:
┌─ Lambda 1 ─┐                     ┌───────────┐     10 real connections     ┌──────────┐
┌─ Lambda 2 ─┐                     │           │ ──────────────────────────  │          │
┌─ Lambda 3 ─┐  ── TCP 5432 ──→   │ RDS Proxy │     (persistent, reused)   │ Database │
│     ...     │  (short-lived)     │ (pooler)  │                             │ (max 100)│
┌─ Lambda 200─┐                     │           │                             │          │
               ← response ──       └───────────┘                             └──────────┘

200 Lambda instances share 10 actual database connections.
Database sees 10 connections, not 200.
```

The flow:
1. Lambda opens a TCP connection to RDS Proxy (not the real database)
2. RDS Proxy picks an available connection from its pool to the real database
3. Lambda sends SQL query through Proxy to the database
4. Database returns results through Proxy to Lambda
5. Lambda disconnects from Proxy
6. Proxy keeps the real database connection open for the next Lambda

**Key behaviors:**
- **Multiplexing:** Many Lambda connections share fewer database connections
- **Connection reuse:** Real connections are never closed and reopened (expensive). They're recycled.
- **Queuing:** If all real connections are busy, Proxy queues the Lambda's request until one frees up (instead of crashing)
- **Failover:** If the database restarts, Proxy automatically reconnects (Lambda doesn't notice)

### RDS Proxy vs Self-Hosted PgBouncer

PgBouncer is an open-source connection pooler that does the same job. The difference is operational:

| Aspect | RDS Proxy (managed) | PgBouncer on EC2 (self-hosted) |
|--------|--------------------|---------------------------------|
| Cost | ~$15/month | ~$3/month (t4g.nano) |
| Setup | Enable in CDK, done | Launch EC2, install, configure, systemd |
| Patching | AWS handles it | You SSH in and update |
| Monitoring | CloudWatch built-in | Install CloudWatch agent manually |
| High availability | Multi-AZ automatic | Single instance = single point of failure |
| If it crashes | AWS restarts in <1s | systemd restarts process, but EC2 death = downtime |
| TLS | Automatic | Manual cert configuration |

---

## How Aurora Data API Avoids Proxying Entirely

Aurora Serverless v2 takes a different approach: instead of Lambda opening a TCP connection to the database, it makes an **HTTPS request** to an AWS API endpoint.

```
Lambda with Aurora Data API:
┌─ Lambda 1 ─┐                                          ┌──────────────────┐
┌─ Lambda 2 ─┐    HTTPS (stateless, like calling S3)    │ Aurora Serverless│
┌─ Lambda 3 ─┐  ──────────────────────────────────────  │ + Data API       │
│     ...     │     no TCP connections from Lambda       │ (AWS manages     │
┌─ Lambda 200─┐                                          │  internal pool)  │
                                                         └──────────────────┘
```

Your Lambda code looks like this:

```python
import boto3

client = boto3.client('rds-data')

response = client.execute_statement(
    resourceArn='arn:aws:rds:us-east-1:123456:cluster:betterself',
    secretArn='arn:aws:secretsmanager:us-east-1:123456:secret:db-creds',
    database='betterself',
    sql='SELECT * FROM calendar_events WHERE user_id = :uid AND start_time > :start',
    parameters=[
        {'name': 'uid', 'value': {'stringValue': 'abc-123'}},
        {'name': 'start', 'value': {'stringValue': '2026-03-01'}}
    ]
)

rows = response['records']  # List of rows, each is a list of column values
```

No `psycopg2`, no `asyncpg`, no connection strings, no pool configuration. Just `boto3` (the AWS SDK, already available in every Lambda).

**Why it works:** AWS runs its own connection pool inside the Data API service. Your Lambda never touches the database directly -- it talks to an HTTPS endpoint that translates your SQL into database operations and returns results.

**The tradeoff:** Aurora's minimum cost is ~$43/month (0.5 ACU floor), which is $28/month more than our RDS + Proxy setup. The Data API also has less mature ORM support (SQLAlchemy adapters exist but are less battle-tested than standard PostgreSQL drivers).

---

## Our Final Architecture

```
┌──────────────┐                          ┌──────────────┐                     ┌───────────────────┐
│              │     TCP 5432             │              │     TCP 5432        │                   │
│  FastAPI     │ ──────────────────────→  │  RDS Proxy   │ ─────────────────→  │  RDS PostgreSQL   │
│  Lambda      │     (short-lived,        │  (~$15/mo)   │  (persistent,       │  (db.t3.micro     │
│              │      multiplexed)        │              │   reused)           │   FREE for 12mo)  │
└──────────────┘                          └──────────────┘                     └───────────────────┘
       │                                         │                                      │
       │ Uses SQLAlchemy +                       │ Pools ~10 real                        │ Stores all 9 tables:
       │ asyncpg driver                          │ connections across                    │ users, blocking_profiles,
       │                                         │ all Lambda instances                  │ blocking_sessions,
       │ Connection string                       │                                      │ calendar_events, tasks,
       │ points to Proxy                         │ Credentials from                     │ habits, habit_check_ins,
       │ endpoint (NOT RDS                       │ Secrets Manager                      │ ai_conversations,
       │ directly)                               │                                      │ daily_briefings
       │                                         │                                      │
       ▼                                         ▼                                      ▼
  Security Group:                          Security Group:                        Security Group:
  Outbound 5432 → Proxy SG               Inbound 5432 from Lambda SG            Inbound 5432 from Proxy SG
  Outbound 443 → Internet                 Outbound 5432 → RDS SG                (nothing else)
```

### Cost Summary

| Component | Monthly Cost | Notes |
|-----------|-------------|-------|
| RDS PostgreSQL (db.t3.micro) | $0 | Free tier, 12 months |
| RDS Proxy | ~$15 | Scales with DB instance size |
| 20GB storage (gp3) | $0 | Free tier |
| **After 12-month free tier** | **~$27** | db.t4g.micro (~$12) + Proxy (~$15) |

### When We'd Reconsider

- **Traffic exceeds free tier limits:** Evaluate Aurora Serverless v2 (auto-scales, Data API eliminates Proxy need, but $43/month minimum)
- **Need horizontal read scaling:** Add RDS read replicas ($12/month each)
- **Specific tables hit DynamoDB-scale volume:** Move just those tables to DynamoDB (e.g., AI conversation logs at 10K+ writes/second)

---

## PostgreSQL Concepts Used in BetterSelf

### JSONB Columns

PostgreSQL has a `JSONB` type that stores JSON data in a binary format. It's indexable and queryable -- giving you NoSQL flexibility within SQL:

```sql
-- Store flexible preferences as JSONB
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE,
    preferences JSONB DEFAULT '{}'
);

-- Query inside the JSON
SELECT * FROM users
WHERE preferences->>'theme' = 'dark'
  AND (preferences->'notifications'->>'enabled')::boolean = true;

-- Index a specific JSON path for fast lookups
CREATE INDEX idx_users_theme ON users ((preferences->>'theme'));
```

We use JSONB for: user preferences, blocking profile schedules, app tokens, calendar sync metadata, AI conversation messages, and daily briefing content.

### UUID Primary Keys

Every table uses UUID (Universally Unique Identifier) as the primary key instead of auto-incrementing integers:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ...
);
-- Generates: 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'
```

**Why UUIDs over integers:**
- Can be generated client-side (no round-trip to DB)
- No sequential ID enumeration attacks (can't guess `user/2` from `user/1`)
- Safe to merge data from multiple sources (no ID collisions)

### Alembic Migrations

Alembic tracks database schema changes as versioned Python scripts. Instead of manually running `ALTER TABLE`, you write migration files:

```python
# migrations/versions/001_initial_schema.py
def upgrade():
    op.create_table('users',
        sa.Column('id', sa.UUID(), primary_key=True),
        sa.Column('email', sa.Text(), unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('users')
```

Run `alembic upgrade head` to apply all pending migrations. Run `alembic downgrade -1` to roll back the last one. Every migration is tracked in an `alembic_version` table in the database.

---

## Quick Reference: Decision Matrix

| Factor | DynamoDB | Aurora Serverless v2 | RDS + RDS Proxy |
|--------|----------|---------------------|-----------------|
| MVP monthly cost | ~$0-10 | ~$43+ | **~$15 (free tier RDS)** |
| Post-free-tier cost | ~$0-10 | ~$43+ | ~$27 |
| Connection management | None needed | Data API (free) | RDS Proxy (~$15/mo) |
| JOINs / aggregations | No | Yes | **Yes** |
| Full-text search | No (need OpenSearch) | Yes (built-in) | **Yes (built-in)** |
| ORM support | Limited (boto3) | Limited (Data API adapter) | **Full (SQLAlchemy + asyncpg)** |
| Future migration needed | Yes (when adding analytics/social) | No | **No** |
| Lambda cold start impact | None (HTTP) | None (HTTP/Data API) | ~10-35ms (TCP + TLS) |
| Operational complexity | Low | Medium | **Medium** |
