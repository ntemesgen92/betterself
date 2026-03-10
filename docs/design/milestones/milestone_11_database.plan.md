# Milestone 11: Database Setup

## Status
Not Started

## Goal
Set up RDS PostgreSQL instance, RDS Proxy for Lambda connection pooling, Secrets Manager for credentials, and Alembic for schema migrations. All application tables are created and ready for use by backend APIs.

## Dependencies
Milestone 9 (CDK Foundation -- VPC and security groups)

## Plan
- Create RDS PostgreSQL instance (db.t3.micro free tier) in private subnets
- Configure RDS Proxy for Lambda connection pooling
- Store database credentials in Secrets Manager
- Set up Alembic migration framework
- Write initial migration with all application tables
- Configure automated backups and point-in-time recovery

## Key Files
| File | Description |
|------|-------------|
| infrastructure/stacks/database_stack.py | RDS instance, RDS Proxy, Secrets Manager, subnet groups |
| api/alembic.ini | Alembic configuration |
| api/migrations/env.py | Alembic environment setup |
| api/migrations/versions/001_initial_schema.py | Initial schema migration |
| api/models/base.py | SQLAlchemy Base, common mixins |
| api/db/session.py | Database session factory (uses RDS Proxy endpoint) |

## Implementation Details
1. **RDS Instance**: PostgreSQL 15, db.t3.micro (free tier), private subnets, Multi-AZ disabled for dev (enable for prod), 20GB gp3 storage, automated backups enabled (7-day retention)
2. **Secrets Manager**: Auto-generate DB master password, store in Secrets Manager, CDK integration for automatic rotation
3. **RDS Proxy**: Target the RDS instance, use Secrets Manager credentials, IAM authentication enabled, idle client timeout 1800s, max connections percent 100
4. **Alembic setup**: Initialize Alembic with async SQLAlchemy support, configure to read DB URL from environment variable (RDS Proxy endpoint)
5. **Initial migration (001_initial_schema.py)**:
   - `users` -- id (UUID), email (UNIQUE), cognito_sub (UNIQUE), display_name, preferences (JSONB), subscription_status, created_at, updated_at
   - `blocking_profiles` -- id (UUID), user_id (FK), name, app_tokens (JSONB), schedule (JSONB), is_active, created_at, updated_at
   - `blocking_sessions` -- id (UUID), user_id (FK), profile_id (FK), start_time, end_time, duration_seconds, was_overridden, created_at
   - `ai_conversations` -- id (UUID), user_id (FK), conversation_id (UUID), messages (JSONB), tokens_used, created_at
   - `calendar_events` -- id (UUID), user_id (FK), external_id, source (enum: apple, google, ai), title, description, location, start_time, end_time, all_day (bool), recurrence_rule, is_ai_created, sync_metadata (JSONB), created_at, updated_at
   - `tasks` -- id (UUID), user_id (FK), title, description, priority (enum: low, medium, high, urgent), status (enum: todo, in_progress, done, cancelled), due_date, ai_suggested (bool), created_at, updated_at
   - `habits` -- id (UUID), user_id (FK), name, frequency (enum: daily, weekly), current_streak, longest_streak, last_check_in, created_at
   - `habit_check_ins` -- id (UUID), habit_id (FK), user_id (FK), checked_in_at, created_at
   - `daily_briefings` -- id (UUID), user_id (FK), briefing_date (DATE), content (JSONB), created_at; UNIQUE constraint on (user_id, briefing_date)
6. **Indexes**: Created in the migration -- composite indexes on (user_id, start_time) for sessions and events, (user_id, status, due_date) for tasks, (habit_id, checked_in_at) for check-ins
7. **SQLAlchemy models**: Define models in `api/models/` using SQLAlchemy 2.0 declarative style with `mapped_column`, matching the migration schema
8. **Session factory**: `api/db/session.py` creates async sessions using `asyncpg` driver, connection string points to RDS Proxy endpoint (not RDS directly)

## Testing
- CDK synth produces valid CloudFormation for RDS, Proxy, and Secrets Manager
- `cdk deploy` creates RDS instance and Proxy successfully
- Can connect to RDS through Proxy endpoint from Lambda
- Alembic migration runs successfully (`alembic upgrade head`)
- All tables created with correct columns, types, constraints, and indexes
- Foreign key relationships enforced (inserting orphan record fails)

## Test Requirements (Definition of Done)
- pytest tests for Alembic migration (upgrade and downgrade)
- pytest tests for SQLAlchemy model creation and validation
- pytest tests for repository CRUD operations against a test database
- Verify RDS Proxy connection from a test Lambda function
- Verify Secrets Manager credential retrieval

## Notes
- **Duration**: 2 days
- **Decision**: Single RDS PostgreSQL database for all tables. Chosen over DynamoDB to support relational queries (JOINs, aggregations, full-text search) needed for analytics, calendar recurrence, and future social features without migration. RDS Proxy eliminates Lambda connection pooling concerns.
- Use `uuid_generate_v4()` PostgreSQL extension for UUID primary keys
- Consider `pg_trgm` extension for future full-text search on conversations
- Lambda connects to RDS Proxy endpoint, never directly to RDS instance
