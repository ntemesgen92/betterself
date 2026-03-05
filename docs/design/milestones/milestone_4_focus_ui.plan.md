# Milestone 4: Focus Mode UI

## Status
Not Started

## Goal
Build the complete Focus tab UI including profile list/grid, profile editor with app picker, active focus session screen with countdown timer, and focus history. All functionality uses mock data; FamilyControls integration comes in Milestone 5.

## Dependencies
- Milestone 1 (Project Setup)
- Milestone 2 (Data Models & Local Storage)
- Milestone 3 (Tab Navigation & Home Dashboard)

## Plan
- FocusHomeView: current session status, profile grid, screen time stats, recent sessions
- ProfileEditorView: profile form with name, icon, mode, schedule, strict mode
- AppPickerView: placeholder for FamilyActivityPicker (real picker in M5)
- ActiveSessionView: full-screen countdown timer, motivational quotes, breathing animation
- FocusHistoryView: past sessions list

## Key Files
| File | Description |
|------|-------------|
| FocusHomeView.swift | Focus tab main screen |
| FocusViewModel.swift | Focus state and profile management |
| ProfileEditorView.swift | Create/edit blocking profile form |
| AppPickerView.swift | App selection (placeholder until M5) |
| ActiveSessionView.swift | Active session countdown UI |
| FocusHistoryView.swift | Past sessions list |

## Implementation Details

1. **FocusHomeView**
   - Current session status card: shows circular timer if session active, else "No active session"
   - Grid of saved profiles as quick-start buttons (tap to start session with that profile)
   - Today's screen time stats bar: placeholder for DeviceActivity data
   - Recent sessions list: last 5–10 sessions with profile name, duration, completion status
   - FAB or prominent "New Profile" button

2. **ProfileEditorView**
   - Form fields: profile name, icon picker (emoji or SF Symbol), mode selector (Timed / Cold Turkey / Allowlist)
   - Schedule picker: select days of week, time range (start–end)
   - Strict mode toggle with explanation sheet (what happens when user tries to override)
   - "Select Apps" button → AppPickerView
   - Save/Cancel navigation bar actions

3. **AppPickerView**
   - Placeholder UI: categorized app list with search bar
   - Mock categories: Social, Entertainment, Games, Productivity
   - Checkbox-style selection, "Select All" per category
   - Will be replaced with FamilyActivityPicker in Milestone 5

4. **ActiveSessionView**
   - Full-screen immersive layout
   - Circular progress ring countdown timer (matches profile duration)
   - Motivational quotes rotation (e.g., every 30 seconds)
   - Blocked attempts counter (mock increment for now)
   - Subtle breathing animation background (scale/pulse)
   - Override button (wired to AI gatekeeper in M5)
   - End Session button when time completes

5. **FocusHistoryView**
   - List of past sessions: date, profile used, duration, completion status (completed vs overridden)
   - Filter by date range or profile
   - Swipe to delete (optional)

## Testing
- All screens render correctly
- Timer counts down accurately when session is active
- Profile CRUD works with mock data (create, edit, delete)
- Navigation flow: Home → Profile Editor → App Picker → Back; Start Session → Active Session → End
- Breathing animation and quotes display without performance issues

## Notes
- Duration: 4 days
