# Milestone 11: Database Setup

## Status
Not Started

## Goal
DynamoDB tables + GSIs, CDK definitions (Aurora deferred to post-MVP). Table schemas are defined and ready for application use, with appropriate indexes, access patterns, and recovery options.

## Dependencies
Milestone 9 (CDK Foundation)

## Plan
- Create DynamoDB tables for all entities: Users, BlockingProfiles, BlockingSessions, AIConversations, CalendarEvents, Tasks, Habits, DailyBriefings
- Design GSIs for each table's access patterns
- Configure billing, TTLs, and point-in-time recovery
- Set up VPC endpoints for DynamoDB

## Key Files
| File | Description |
|------|-------------|
| infrastructure/stacks/database_stack.py | DynamoDB tables, GSIs, VPC endpoints |

## Implementation Details
1. **Users table**: PK: user_id. Stores profile, preferences, subscription status.
2. **BlockingProfiles table**: PK: user_id, SK: profile_id. Stores app-blocking profile configs.
3. **BlockingSessions table**: PK: user_id, SK: start_time. GSI: profile_id-index (PK: profile_id, SK: start_time) for querying sessions by profile.
4. **AIConversations table**: PK: user_id, SK: timestamp. TTL: 90 days.
5. **CalendarEvents table**: PK: user_id, SK: event_id. GSI: user_date-index (PK: user_id, SK: start_time) for date-range queries. GSI: source-index (PK: user_id, SK: source) for filtering by calendar source. Stores recurrence rules, AI-created flag, sync metadata.
6. **Tasks table**: PK: user_id, SK: task_id. GSI: status-due-index (PK: user_id#status, SK: due_date) for filtered queries by status and due date. GSI: priority-index (PK: user_id, SK: priority) for prioritization queries.
7. **Habits table**: PK: user_id, SK: habit_id. Stores frequency, streak counter, last check-in date. HabitCheckIns stored as items with PK: user_id#habit_id, SK: date.
8. **DailyBriefings table**: PK: user_id, SK: date. Stores generated briefing content and metadata.
9. **DynamoDB configuration**: On-demand billing for all tables, point-in-time recovery enabled, TTL on AIConversations (90 days).
10. **VPC endpoints**: Gateway endpoint for DynamoDB (saves NAT costs).

## Testing
- All DynamoDB tables created with correct schemas and GSIs
- Read/write operations work on all tables
- GSI queries return correct results for each access pattern
- TTL configured correctly on AIConversations

## Notes
- **Duration**: 2 days
- **Decision**: DynamoDB-only for MVP. Aurora PostgreSQL deferred to post-MVP. If complex relational queries are needed later (e.g., advanced analytics, cross-entity joins), Aurora can be introduced without changing the application data model significantly.
