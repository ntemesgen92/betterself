# Milestone 14: User & Auth API

## Status
Not Started

## Goal
Implement user registration, login, profile management, and subscription status endpoints. Auth middleware validates Cognito JWT tokens and user records are stored in DynamoDB.

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
2. **POST /auth/register**: Create user record in DynamoDB after Cognito signup confirmation (webhook or post-confirmation Lambda trigger)
3. **GET /users/me**: Return current user profile from DynamoDB
4. **PUT /users/me**: Update user profile (name, preferences)
5. **PUT /users/me/preferences**: Update AI preferences, notification settings, calendar connections
6. **GET /users/me/subscription**: Return subscription tier and usage stats (AI queries remaining today)
7. **DELETE /users/me**: Account deletion (GDPR compliance) - removes DynamoDB records, anonymizes Aurora data, triggers Cognito user deletion
8. **Pydantic models**: Request/response validation
9. **Cognito trigger**: Post-confirmation Lambda trigger to auto-create DynamoDB user record

## Testing
- Registration creates user in DynamoDB
- JWT auth middleware rejects invalid tokens
- Profile CRUD works
- Account deletion removes all user data
- Rate limiting on auth endpoints works

## Notes
- **Duration**: 2 days
