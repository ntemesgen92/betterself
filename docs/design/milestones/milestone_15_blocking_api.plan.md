# Milestone 15: Blocking Rules API

## Status
Not Started

## Goal
Implement CRUD endpoints for blocking profiles and session logging. Enables the iOS app to sync blocking rules with the cloud and retrieve aggregated focus statistics.

## Dependencies
Milestones 12 (Lambda & API Gateway), 14 (User & Auth API)

## Plan
- Implement profile CRUD (create, list, get, update, delete)
- Add session logging endpoint
- Create stats aggregation endpoint
- Ensure authorization for user-scoped data access

## Key Files
| File | Description |
|------|-------------|
| api/routers/blocking.py | Blocking profile and session endpoints |
| api/models/blocking.py | Blocking profile and session Pydantic models |

## Implementation Details
1. **POST /blocking/profiles**: Create new profile (name, mode, blocked_apps, allowed_apps, schedule, strict_mode)
2. **GET /blocking/profiles**: List all profiles for authenticated user
3. **GET /blocking/profiles/{id}**: Get specific profile
4. **PUT /blocking/profiles/{id}**: Update profile
5. **DELETE /blocking/profiles/{id}**: Delete profile
6. **POST /blocking/sessions**: Log completed focus session (profile_id, start_time, end_time, override_attempts, completed)
7. **GET /blocking/sessions**: List sessions with optional date range filter
8. **GET /blocking/stats**: Aggregated stats (total focus time today/week/month, average session length, completion rate, most blocked apps)
9. **Storage**: PostgreSQL blocking_profiles and blocking_sessions tables (via SQLAlchemy)
10. **Input validation**: Schedule must have valid days/times, blocked_apps is array of app bundle identifiers or category tokens

## Testing
- Full CRUD lifecycle for profiles
- Session logging creates records
- Stats endpoint returns correct aggregations
- Authorization ensures users can only access their own data

## Test Requirements (Definition of Done)
- pytest tests for full CRUD lifecycle on /blocking/profiles (create, list, get, update, delete)
- pytest tests for POST /blocking/sessions logging and GET with date range filter
- pytest tests for /blocking/stats aggregation accuracy
- pytest tests for auth middleware (reject unauthenticated, reject cross-user access)
- pytest tests for input validation (invalid schedule, empty blocked_apps)

## Notes
- **Duration**: 2 days
