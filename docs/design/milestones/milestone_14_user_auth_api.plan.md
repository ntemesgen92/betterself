# Milestone 14: User & Auth API

## Status
Not Started

## Goal
Implement user registration, login, profile management, and subscription status endpoints. Auth middleware validates Cognito JWT tokens and user records are stored in PostgreSQL.

## Dependencies
Milestones 10 (Auth Infrastructure), 12 (Lambda & API Gateway)

## Plan
- Implement auth middleware for JWT validation
- Create user registration and profile CRUD endpoints
- Add subscription status and account deletion
- Set up Cognito post-confirmation trigger for user creation

## Key Files
| File | Description |
|------|-------------|
| api/routers/auth.py | Auth endpoints |
| api/routers/users.py | User profile and subscription endpoints |
| api/models/user.py | Pydantic user models |
| api/utils/auth.py | JWT validation, claims extraction |

## Implementation Details
1. **Auth middleware**: Extract and validate Cognito JWT from Authorization header, decode user claims (sub, email, custom attributes)
2. **POST /auth/register**: Create user record in PostgreSQL after Cognito signup confirmation (webhook or post-confirmation Lambda trigger)
3. **GET /users/me**: Return current user profile from PostgreSQL
4. **PUT /users/me**: Update user profile (name, preferences)
5. **PUT /users/me/preferences**: Update AI preferences, notification settings, calendar connections
6. **GET /users/me/subscription**: Return subscription tier and usage stats (AI queries remaining today)
7. **DELETE /users/me**: Account deletion (GDPR compliance) - removes all PostgreSQL records across tables, triggers Cognito user deletion
8. **Pydantic models**: Request/response validation
9. **Cognito trigger**: Post-confirmation Lambda trigger to auto-create PostgreSQL user record

## Testing
- Registration creates user in PostgreSQL
- JWT auth middleware rejects invalid tokens
- Profile CRUD works
- Account deletion removes all user data
- Rate limiting on auth endpoints works

## Test Requirements (Definition of Done)
- pytest tests for POST /auth/register (success, duplicate, invalid input)
- pytest tests for GET/PUT /users/me profile CRUD
- pytest tests for auth middleware rejection (missing token, expired token, malformed token)
- pytest test for DELETE /users/me data removal verification
- pytest test for rate limiting on auth endpoints

## Notes
- **Duration**: 2 days
- Storage layer uses SQLAlchemy models with asyncpg via RDS Proxy, not boto3/DynamoDB
