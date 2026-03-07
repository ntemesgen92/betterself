# Milestone 16: Calendar API

## Status
Not Started

## Goal
Implement calendar event CRUD, external calendar sync management, and AI-created event handling. Events stored in DynamoDB with GSIs for date-range queries, with support for recurrence, conflict detection, and AI-powered schedule optimization.

## Dependencies
Milestones 11 (Database Setup), 12 (Lambda & API Gateway), 14 (User & Auth API)

## Plan
- Implement event CRUD endpoints
- Add sync and conflict detection endpoints
- Create AI-powered schedule optimization endpoint
- Handle recurrence rules and AI-created event metadata

## Key Files
| File | Description |
|------|-------------|
| api/routers/calendar.py | Calendar event and sync endpoints |
| api/models/calendar.py | Event and sync Pydantic models |
| api/services/calendar_service.py | Event logic, sync merge, conflict detection |

## Implementation Details
1. **POST /calendar/events**: Create event (title, start/end time, location, description, recurrence, source)
2. **GET /calendar/events**: List events with date range filter, source filter
3. **GET /calendar/events/{id}**: Get event detail
4. **PUT /calendar/events/{id}**: Update event
5. **DELETE /calendar/events/{id}**: Delete event
6. **POST /calendar/sync**: Trigger sync from iOS (receives batch of local calendar events, merges with cloud state)
7. **GET /calendar/conflicts**: Detect scheduling conflicts in date range
8. **POST /calendar/optimize**: AI-powered schedule optimization (calls Bedrock to analyze schedule and suggest improvements), returns list of proposed changes
9. **Storage**: DynamoDB CalendarEvents table with user_date-index GSI for date-range queries
10. **Recurrence**: Store RRULE-compatible recurrence rules, expand occurrences on read
11. **AI events**: Flag ai_created=true and link to AI conversation that created them

## Testing
- Event CRUD works
- Date range queries return correct events
- Sync merges correctly
- Conflict detection identifies overlapping events
- AI optimization returns valid suggestions

## Test Requirements (Definition of Done)
- pytest tests for event CRUD endpoints (create, list, get, update, delete)
- pytest tests for date range query filtering and boundary conditions
- pytest tests for conflict detection (overlapping events, adjacent events, no conflict)
- pytest tests for sync merge logic (new/updated/deleted events, idempotent replay)
- pytest test for recurrence rule storage and occurrence expansion

## Notes
- **Duration**: 3 days
