# Milestone 21: Auth Integration (iOS)

## Status
Not Started

## Goal
Integrate AWS Cognito SDK in the Swift app, implement sign-in/sign-up flows for email, Apple, and Google, with token management and secure storage in Keychain. Users can authenticate and remain signed in across app launches.

## Dependencies
Milestones 10 (Auth Infrastructure), 14 (User & Auth API), iOS Milestones 1–3

## Plan
- Add AWS Amplify Auth SDK via Swift Package Manager
- Configure Amplify with Cognito pool IDs and API Gateway endpoint
- Implement SignInView and SignUpView with email, Apple, Google
- Build AuthService with token refresh and Keychain storage
- Wire auth state to app root and API token injection

## Key Files
| File | Description |
|------|-------------|
| AuthService.swift | Sign-in, sign-up, sign-out, token management |
| SignInView.swift | Sign-in form with Apple/Google buttons |
| SignUpView.swift | Sign-up form with verification |
| KeychainManager.swift | Secure token storage |

## Implementation Details

1. **Add AWS Amplify Auth SDK** (or AWSCognitoIdentityProvider directly) via Swift Package Manager

2. **Configure Amplify** with Cognito pool IDs and API Gateway endpoint

3. **SignInView**: Email/password form, "Sign in with Apple" button (ASAuthorizationAppleIDProvider), "Sign in with Google" button (GoogleSignIn SDK), divider between methods, "Create account" link

4. **SignUpView**: Email, password, confirm password, name fields; email verification code step

5. **AuthService**: sign-in/sign-up/sign-out methods, token refresh handling, token storage in Keychain via KeychainManager, current user state as @Published property, auto-sign-in on app launch if tokens are valid

6. **Auth state management**: Use AuthService as @Observable in app root; show onboarding/sign-in if not authenticated, main tab view if authenticated

7. **Token injection**: APIClient reads access token from AuthService for all API calls

## Testing
- Email sign-up with verification works
- Sign in with Apple flow works
- Sign in with Google flow works
- Token refresh works transparently
- Sign-out clears Keychain
- Unauthorized API calls redirect to sign-in

## Notes
- **Duration**: 2 days
