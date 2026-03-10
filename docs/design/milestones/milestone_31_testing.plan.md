# Milestone 31: Testing & QA

## Status
Not Started

## Goal
Integration/E2E tests only (unit tests already written per-milestone). Cross-system flow verification, TestFlight beta distribution.

## Dependencies
All previous milestones

## Plan
- UI tests (XCUITest) for onboarding, focus flow, calendar, AI chat, settings, widget deep links
- Integration tests against staging backend for API, auth, calendar sync, AI
- Backend integration tests (pytest) for cross-service flows, DynamoDB, notifications
- Performance testing: launch time <2s, API <500ms CRUD/<3s AI, 1000+ events
- TestFlight: internal + external beta, feedback form, crash monitoring

## Key Files
| File | Description |
|------|-------------|
| Tests/UITests/ | End-to-end UI test flows |
| Tests/IntegrationTests/ | API and backend integration tests |

## Implementation Details

1. **UI tests (XCUITest)**: Test onboarding flow end-to-end. Test focus session lifecycle (create profile → start session → timer → complete). Test calendar event creation. Test AI chat send message flow. Test settings navigation. Test widget deep links.

2. **Integration tests**: Test API client against staging backend. Test auth flow (sign up → sign in → access API). Test calendar sync round-trip. Test AI chat end-to-end.

3. **Backend integration tests (pytest)**: Test cross-service flows (e.g., AI creates event → appears in calendar). Test DynamoDB operations across tables. Test Bedrock integration with mocked responses. Test notification sending. (Unit tests for individual routers/services already written in their respective milestones.)

4. **Performance testing**: Measure app launch time (target <2s). Measure API response times (target <500ms for CRUD, <3s for AI). Test with 1000+ calendar events.

5. **TestFlight**: Configure TestFlight in App Store Connect. Invite internal testers (team). Invite external beta testers (10-20 users). Create feedback form. Monitor crash reports.

## Testing
- All test suites pass
- Code coverage meets targets
- TestFlight build installs and runs on testers' devices
- Crash-free rate >99%
- Critical user flows work on iPhone SE through iPhone 16 Pro Max

## Notes
Duration: 3 days
