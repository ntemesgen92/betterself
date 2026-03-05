# Milestone 27: Live Activities

## Status
Not Started

## Goal
Implement Live Activities for lock screen focus session timer and Dynamic Island support during active focus sessions.

## Dependencies
- Milestone 4 (Focus UI)
- Milestone 5 (Family Controls)

## Plan
- Define ActivityAttributes with profile name, start/end time, ContentState with remaining seconds and blocked attempts
- Live Activity UI: compact (Dynamic Island), expanded, and lock screen views
- Start Live Activity when focus session begins from ActiveSessionView/FocusViewModel
- Update every minute with remaining time and blocked attempt count
- End Live Activity with completion summary, auto-dismiss after 30 seconds
- Handle edge cases: app killed, device restart, session extending past midnight

## Key Files
| File | Description |
|------|-------------|
| FocusLiveActivity.swift | Live Activity view definitions |
| FocusActivityAttributes.swift | Activity attributes and state |
| ActiveSessionView.swift | Start/stop Live Activity (update) |

## Implementation Details

1. **Define ActivityAttributes**: FocusActivityAttributes with profile name, start time, end time, and ContentState with remaining seconds, blocked attempts count.

2. **Live Activity UI**: Compact view (Dynamic Island) shows timer countdown and focus profile icon. Expanded view shows full timer ring + profile name + blocked attempts + motivational text. Lock screen view shows large timer with profile name.

3. **Start Live Activity** when focus session begins: Called from ActiveSessionView or FocusViewModel when session starts.

4. **Update Live Activity**: Push updates every minute with remaining time and blocked attempt count. Use ActivityKit push tokens for remote updates (or local timer updates).

5. **End Live Activity**: When session completes or is overridden, show completion summary (duration, blocked attempts) in final content. Auto-dismiss after 30 seconds.

6. **Dynamic Island**: Minimal shows timer countdown. Compact leading shows focus icon. Compact trailing shows remaining time. Expanded shows full timer + profile name.

7. **Edge cases**: App killed during session (Live Activity persists), device restart, session extending past midnight.

## Testing
- Live Activity appears on lock screen when session starts
- Dynamic Island shows timer correctly
- Updates reflect current time remaining
- Blocked attempts update in real time
- Completion summary displays correctly
- Activity ends when session ends

## Notes
Duration: 2 days
