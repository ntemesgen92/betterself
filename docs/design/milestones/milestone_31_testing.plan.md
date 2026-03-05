# Milestone 31: Testing & QA

## Status
Not Started

## Goal
Comprehensive testing across unit tests, UI tests, integration tests, and TestFlight beta distribution to ensure app quality before App Store submission.

## Dependencies
All previous milestones

## Plan
- Unit tests (XCTest) for ViewModels, services, models; target 70%+ coverage
- UI tests (XCUITest) for onboarding, focus flow, calendar, AI chat, settings, widget deep links
- Integration tests against staging backend for API, auth, calendar sync, AI
- Backend tests (pytest) for routers, Bedrock, DynamoDB, Aurora, notifications
- Performance testing: launch time <2s, API <500ms CRUD/<3s AI, 1000+ events
- TestFlight: internal + external beta, feedback form, crash monitoring

## Key Files
| File | Description |
|------|-------------|
| Tests/UnitTests/ | ViewModel, service, model unit tests |
| Tests/UITests/ | End-to-end UI test flows |
| Tests/IntegrationTests/ | API and backend integration tests |

## Implementation Details

1. **Unit tests (XCTest)**: Test all ViewModels (HomeViewModel, FocusViewModel, CalendarViewModel, AIChatViewModel). Test services (AuthService, BlockingService, CalendarService, AIService) with mocked dependencies. Test data models and repository logic. Test SyncEngine conflict resolution. Test streak calculation. Target 70%+ code coverage.

2. **UI tests (XCUITest)**: Test onboarding flow end-to-end. Test focus session lifecycle (create profile → start session → timer → complete). Test calendar event creation. Test AI chat send message flow. Test settings navigation. Test widget deep links.

3. **Integration tests**: Test API client against staging backend. Test auth flow (sign up → sign in → access API). Test calendar sync round-trip. Test AI chat end-to-end.

4. **Backend tests (pytest)**: Unit tests for all routers. Test Bedrock integration with mocked responses. Test DynamoDB operations. Test Aurora queries. Test notification sending.

5. **Performance testing**: Measure app launch time (target <2s). Measure API response times (target <500ms for CRUD, <3s for AI). Test with 1000+ calendar events.

6. **TestFlight**: Configure TestFlight in App Store Connect. Invite internal testers (team). Invite external beta testers (10-20 users). Create feedback form. Monitor crash reports.

## Testing
- All test suites pass
- Code coverage meets targets
- TestFlight build installs and runs on testers' devices
- Crash-free rate >99%
- Critical user flows work on iPhone SE through iPhone 16 Pro Max

## Notes
Duration: 3 days
