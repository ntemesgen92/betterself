# Milestone 26: iOS Widgets

## Status
Not Started

## Goal
Build home screen widgets using WidgetKit: next event widget, focus timer widget, and daily progress widget.

## Dependencies
- Milestone 3 (Navigation)
- Milestone 4 (Focus UI)
- Milestone 6 (Calendar UI)

## Plan
- Create Widget Extension target in Xcode
- Shared data via App Groups for SwiftData between main app and widget extension
- NextEventWidget: small/medium, next upcoming event with title, time, countdown
- FocusTimerWidget: small/medium, active session with circular progress or "Start Focus" prompt
- DailyProgressWidget: medium/large, today's productivity summary with ring/bar charts
- Headspace-inspired design: rounded corners, soft colors, SF Pro Rounded
- Deep links from widgets to relevant app screens
- Widget configuration for focus profile or calendar selection

## Key Files
| File | Description |
|------|-------------|
| BetterSelfWidgets/FocusTimerWidget.swift | Focus session widget |
| BetterSelfWidgets/NextEventWidget.swift | Next event widget |
| BetterSelfWidgets/DailyProgressWidget.swift | Daily progress summary widget |
| BetterSelfWidgets/WidgetBundle.swift | Widget bundle registration |

## Implementation Details

1. **Create Widget Extension target** in Xcode.

2. **Shared data via App Groups**: Create an App Group container to share SwiftData between main app and widget extension.

3. **NextEventWidget**: Small and medium sizes. Shows next upcoming calendar event with title, time, and countdown. Uses TimelineProvider to update when next event changes. Color-coded by calendar source.

4. **FocusTimerWidget**: Small and medium sizes. Shows active focus session with circular progress ring and remaining time. When no session active, shows "Start Focus" prompt. Updates every minute via TimelineProvider.

5. **DailyProgressWidget**: Medium and large sizes. Shows today's productivity summary: focus time completed vs goal, tasks completed, habit check-ins done. Uses ring/bar charts.

6. **Design**: Match the Headspace-inspired aesthetic — rounded corners, soft colors, SF Pro Rounded.

7. **Deep links**: Tapping widgets opens the relevant screen in the app (e.g., focus timer widget opens Active Session).

8. **Widget configuration**: Use WidgetConfigurationIntent for user to select which focus profile or calendar to display.

## Testing
- All widgets render in all supported sizes
- Data updates from App Group correctly
- Deep links navigate correctly
- Widgets update on schedule
- Dark mode renders correctly

## Notes
Duration: 3 days
