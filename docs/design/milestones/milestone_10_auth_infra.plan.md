# Milestone 10: Auth Infrastructure

## Status
Not Started

## Goal
Deploy Cognito user pool with email/password authentication plus Sign in with Apple and Google sign-in. Configure API Gateway with Cognito authorizer for protecting backend endpoints.

## Dependencies
Milestone 9 (CDK Foundation)

## Plan
- Create Cognito User Pool with email verification and password policy
- Configure identity providers for Apple and Google
- Set up Cognito App Client with OAuth 2.0 flows
- Deploy API Gateway with Cognito JWT authorizer
- Configure CORS for development

## Key Files
| File | Description |
|------|-------------|
| infrastructure/stacks/auth_stack.py | Cognito User Pool, identity providers, app client |
| infrastructure/stacks/api_stack.py | API Gateway with Cognito authorizer |

## Implementation Details
1. **Cognito User Pool**: Email as username, required email verification, password policy (8+ chars, mixed case, numbers), custom attributes (subscription_tier, onboarding_completed)
2. **Identity providers**: Sign in with Apple (requires Apple Developer setup), Google Sign-In (requires Google Cloud Console setup)
3. **Cognito App Client**: OAuth 2.0 flows (authorization code grant)
4. **API Gateway**: HTTP API (for lower cost) with Cognito JWT authorizer
5. **CORS**: Configure for development
6. **Custom domain**: Optional for MVP

## Testing
- Cognito sign-up/sign-in with email works
- Apple/Google federated sign-in configured
- API Gateway rejects unauthorized requests
- API Gateway accepts valid JWT tokens

## Notes
- **Duration**: 2 days
- Apple Developer and Google Cloud Console accounts need to be set up before this milestone
- Register app IDs and configure OAuth credentials in advance
