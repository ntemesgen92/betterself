# Milestone 11: Database Setup

## Status
Not Started

## Goal
Deploy DynamoDB tables and Aurora Serverless v2 PostgreSQL cluster via CDK. Table schemas are defined and ready for application use, with appropriate indexes and recovery options.

## Dependencies
Milestone 9 (CDK Foundation)

## Plan
- Create DynamoDB tables for Users, BlockingProfiles, BlockingSessions, AIConversations
- Deploy Aurora Serverless v2 PostgreSQL cluster
- Define Aurora table schemas and migration scripts
- Configure Secrets Manager and VPC endpoints

## Key Files
| File | Description |
|------|-------------|
| infrastructure/stacks/database_stack.py | DynamoDB tables, Aurora cluster, Secrets Manager |

## Implementation Details
1. **DynamoDB tables**: Users (PK: user_id), BlockingProfiles (PK: user_id, SK: profile_id), BlockingSessions (PK: user_id, SK: start_time, GSI on profile_id), AIConversations (PK: user_id, SK: timestamp)
2. **DynamoDB configuration**: On-demand billing, point-in-time recovery enabled, TTL on AIConversations (90 days)
3. **Aurora Serverless v2**: PostgreSQL 15, min 0.5 ACU / max 4 ACU (scales to near-zero), deployed in private subnets
4. **Aurora tables**: calendar_events, tasks, habits, daily_briefings, analytics (SQL migration scripts)
5. **Secrets Manager**: Store Aurora credentials
6. **VPC endpoints**: For DynamoDB (saves NAT costs)

## Testing
- DynamoDB tables created with correct schemas and GSIs
- Aurora cluster accessible from Lambda security group
- SQL migrations run successfully
- Read/write operations work

## Notes
- **Duration**: 2 days
- The DynamoDB-only vs DynamoDB+Aurora decision should be finalized here. If query patterns are simple enough, consider dropping Aurora for MVP to reduce cost and complexity. Document the decision.
