# Milestone 28: Siri Shortcuts

## Status
Not Started

## Goal
Implement App Intents for Siri integration: schedule events, start focus sessions, and get daily briefing via voice commands.

## Dependencies
- Milestone 5 (Family Controls)
- Milestone 7 (Calendar Integration)
- Milestone 8 (AI Chat & Voice)

## Plan
- Create App Intents extension target in Xcode
- ScheduleEventIntent: "Hey Siri, schedule [event] with BetterSelf"
- StartFocusIntent: "Hey Siri, start focus with BetterSelf" with optional profile
- DailyBriefingIntent: "Hey Siri, what's my day with BetterSelf"
- StopFocusIntent: "Hey Siri, stop focus" (respects strict mode)
- Shortcuts app integration for automation
- SiriTipView in relevant screens to teach users

## Key Files
| File | Description |
|------|-------------|
| BetterSelfIntents/AppIntents.swift | Intent registration |
| BetterSelfIntents/ScheduleEventIntent.swift | Schedule event via Siri |
| BetterSelfIntents/StartFocusIntent.swift | Start focus session via Siri |
| BetterSelfIntents/DailyBriefingIntent.swift | Daily briefing via Siri |

## Implementation Details

1. **Create App Intents extension target** in Xcode.

2. **ScheduleEventIntent**: "Hey Siri, schedule [event] with BetterSelf" — accepts event title, date, time as parameters. Opens app with pre-filled create event form or sends to AI for smart scheduling.

3. **StartFocusIntent**: "Hey Siri, start focus with BetterSelf" — accepts optional profile name parameter. Starts the named focus session (or default). Shows confirmation with timer in Siri UI.

4. **DailyBriefingIntent**: "Hey Siri, what's my day with BetterSelf" — returns today's briefing as spoken response: schedule summary, top tasks, focus recommendations.

5. **StopFocusIntent**: "Hey Siri, stop focus" — ends current session (respects strict mode by requiring in-app override).

6. **Shortcuts app integration**: All intents appear in Shortcuts app for automation (e.g., "At 9am every weekday, start Work Focus").

7. **Parameterized queries**: Use @Parameter property wrapper for intent parameters. Provide dynamic options (e.g., list of focus profiles).

8. **Siri Tips**: Display SiriTipView in relevant screens to teach users about available shortcuts.

## Testing
- Each Siri command triggers correct behavior
- Parameters resolve correctly
- Shortcuts automation works
- Intents appear in Shortcuts app
- SiriTipViews display appropriately

## Notes
Duration: 2 days
