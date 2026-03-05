# Milestone 6: Calendar UI

## Status
Not Started

## Goal
Build calendar views (month, week, day) with event display, event detail screen, and create event form. Use Headspace-inspired design and mock data from Milestone 2. No calendar sync yet—that comes in Milestone 7.

## Dependencies
- Milestone 1 (Project Setup)
- Milestone 2 (Data Models & Local Storage)
- Milestone 3 (Tab Navigation & Home Dashboard)

## Plan
- CalendarView with month/week/day segmented control
- MonthView: grid with dot indicators, day selection
- WeekView: horizontal time grid with event blocks
- DayView: vertical timeline with event blocks, current time line
- EventDetailView: card layout with actions
- CreateEventView: full event creation form
- Color coding by calendar source

## Key Files
| File | Description |
|------|-------------|
| CalendarView.swift | Container with view mode toggle |
| CalendarViewModel.swift | Selected date, events, view state |
| MonthView.swift | Month grid calendar |
| WeekView.swift | Week time grid |
| DayView.swift | Day timeline |
| EventDetailView.swift | Event detail and actions |
| CreateEventView.swift | Create/edit event form |

## Implementation Details

1. **CalendarView**
   - Segmented control: Month | Week | Day
   - Date navigation (prev/next, today button)
   - Renders MonthView, WeekView, or DayView based on selection
   - Floating "+" button for quick event creation

2. **MonthView**
   - 7-column grid (Sun–Sat or Mon–Sun based on locale)
   - Day cells with date number
   - Dot indicators for days with events (color by primary source)
   - Tap day to select; selection highlighted
   - Scroll to load adjacent months if needed

3. **WeekView**
   - Horizontal time slots (e.g., 6am–10pm)
   - Events displayed as colored blocks with title
   - Vertical scroll through hours
   - Overlapping events stacked or truncated
   - Tap event to open EventDetailView

4. **DayView**
   - Vertical timeline, one column per day
   - Hour markers on left
   - Event blocks as colored segments
   - Current time indicator (horizontal line)
   - Tap event to open detail

5. **Color Coding**
   - Apple Calendar: blue
   - Google Calendar: red
   - AI-created events: purple

6. **EventDetailView**
   - Card-based layout
   - Title, date/time, location, description
   - Source badge (Apple / Google / AI)
   - Edit and Delete buttons
   - Navigate to CreateEventView for edit

7. **CreateEventView**
   - Form: title, date picker, time picker (start/end), location, description
   - Recurrence options: none, daily, weekly, monthly
   - Calendar source selector (for later sync)
   - Save/Cancel actions
   - Validation: end time after start, required title

8. **Data**
   - All views use mock data from MockDataService / repositories
   - CalendarViewModel fetches events for selected date range

## Testing
- Month, week, and day views render correctly
- Event creation form validates input
- Color coding matches calendar source
- Navigation: Calendar → Event Detail → Edit; Calendar → Create Event
- Current time indicator updates in DayView
- Floating "+" opens CreateEventView

## Notes
- Duration: 4 days
