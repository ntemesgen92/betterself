# Milestone 3: Tab Navigation & Home Dashboard

## Status
Not Started

## Goal
Implement 3-tab navigation (Home, Focus, Calendar) and build the Home dashboard with summary cards (daily briefing, next event, active focus, tasks, habits), quick actions, and a settings shell. Establish the primary user entry point.

## Dependencies
- Milestone 1 (Project Setup)
- Milestone 2 (Data Models & Local Storage)

## Plan
- Build TabView with Home, Focus, Calendar tabs using SF Symbols
- Create HomeView with scrollable layout: greeting, briefing, next event, focus session, tasks, habits, quick actions
- Implement HomeViewModel with @Observable macro pulling from repositories
- Build settings shell with placeholder sections
- Use mock data for all cards

## Key Files
| File | Description |
|------|-------------|
| ContentView.swift | Tab bar root, tab switching |
| HomeView.swift | Home dashboard layout and cards |
| HomeViewModel.swift | Home state management, data fetching |
| DailyBriefingCard.swift | Daily briefing summary card |
| QuickActionsView.swift | Start Focus, Talk to AI buttons |
| SettingsView.swift | Settings shell with section placeholders |

## Implementation Details

1. **TabView Structure**
   - Three tabs: Home (house.fill), Focus (flame.fill), Calendar (calendar)
   - Use SF Symbols for tab bar icons
   - Persist selected tab in UserDefaults if desired
   - Replace ContentView from Milestone 1 with tab-based root

2. **HomeView Layout**
   - ScrollView with vertical stack of cards
   - Time-of-day aware greeting header (Morning/Afternoon/Evening, [Name])
   - DailyBriefingCard: AI-generated summary placeholder
   - Next event card: upcoming calendar event
   - Active focus session card: shows if session is running, else hidden
   - Task summary card: count of incomplete tasks, top 3
   - Habit streaks row: horizontal scroll of habit cards with streak counts
   - QuickActionsView: "Start Focus" and "Talk to AI" prominent buttons

3. **HomeViewModel**
   - Use @Observable macro for SwiftUI reactivity
   - Inject repositories (calendar, tasks, habits, blocking, user)
   - Computed properties for greeting, next event, active session, task summary
   - All data from mock/repositories—no hardcoded values in view

4. **Settings Shell**
   - Sections: Account, Notifications, Calendars, Subscription, AI Voice, Theme
   - Each section navigates to placeholder detail screen (or in-place toggle)
   - Use List/Form with navigation links
   - Dark mode toggle in Theme section

5. **Design Consistency**
   - All cards use design system components from Milestone 1
   - Consistent spacing, corner radius, shadows
   - Support light and dark mode via design tokens

## Testing
- Tab switching works correctly
- All cards render with mock data
- Settings screen navigates to all sections
- Dark mode renders properly for Home and Settings
- Empty states handled (e.g., no events, no tasks)

## Notes
- Duration: 3 days
