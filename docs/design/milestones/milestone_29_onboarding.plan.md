# Milestone 29: Onboarding Flow

## Status
Not Started

## Goal
Build guided onboarding screens that collect user goals, schedule preferences, app selection for blocking, calendar connections, and introduce the AI assistant.

## Dependencies
- Milestone 1 (Setup)
- Milestone 5 (Family Controls)
- Milestone 7 (Calendar Integration)
- Milestone 8 (AI Chat & Voice)

## Plan
- Paged onboarding flow with progress dots, back/next, skip option
- Welcome → Goals → Schedule → App Selection → Calendar Connection → Meet AI → Notifications
- Goals influence AI behavior and default settings
- Schedule step configures work hours and productive time blocks
- App Selection creates initial blocking profile via FamilyActivityPicker
- Calendar Connection requests EventKit + Google Calendar
- AI intro step with interactive voice demo
- OnboardingViewModel saves preferences and marks complete
- Headspace-inspired design throughout

## Key Files
| File | Description |
|------|-------------|
| OnboardingFlow.swift | Main onboarding container |
| GoalsStep.swift | Goals selection step |
| ScheduleStep.swift | Schedule preferences step |
| AppSelectionStep.swift | App blocking selection step |
| CalendarConnectionStep.swift | Calendar connection step |
| AIIntroStep.swift | AI assistant introduction step |
| OnboardingViewModel.swift | Onboarding state and persistence |

## Implementation Details

1. **OnboardingFlow**: Horizontal paged scroll with progress dots, back/next navigation, skip option on non-essential steps.

2. **Step 1 - Welcome**: App branding, value proposition ("Your AI-powered productivity partner"), Get Started button.

3. **Step 2 - Goals**: "What do you want to achieve?" Multi-select cards: Reduce screen time, Stay focused at work, Better schedule management, Build healthy habits, Get more done. Selected goals influence AI behavior and default settings.

4. **Step 3 - Schedule**: "When are you most productive?" Time block selector for morning/afternoon/evening preference. Work hours configuration (start/end time, work days). Helps AI schedule around productive hours.

5. **Step 4 - App Selection**: "Which apps distract you most?" Shows FamilyActivityPicker (if FamilyControls authorized) or category selection (Social Media, Games, Entertainment, News). Creates initial blocking profile.

6. **Step 5 - Calendar Connection**: "Connect your calendars" Apple Calendar permission request (EventKit), Google Calendar sign-in option, preview of upcoming events once connected.

7. **Step 6 - Meet Your AI**: "Meet your AI assistant" Interactive demo: AI introduces itself, user can try a voice command ("What does my day look like?"), shows what the AI can do with animated examples.

8. **Step 7 - Notifications**: Request notification permission, show what types of notifications they'll receive.

9. **OnboardingViewModel**: Saves selections to user preferences, creates initial blocking profile, marks onboarding complete.

10. **Headspace-inspired design**: Soft illustrations, calming transitions, one focus per screen.

## Testing
- Full onboarding flow completes successfully
- Goals saved to preferences
- Blocking profile created from app selection
- Calendar connected
- Notifications authorized
- AI demo works
- User can skip and go back

## Notes
Duration: 3 days
