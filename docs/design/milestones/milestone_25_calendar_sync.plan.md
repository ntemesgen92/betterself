# Milestone 25: Calendar Sync (iOS)

## Status
Not Started

## Goal
Implement two-way calendar sync between the iOS app, backend cloud storage, and external calendars (Apple Calendar + Google Calendar) with conflict resolution.

## Dependencies
- Milestone 7 (Calendar Integration)
- Milestone 16 (Calendar API)
- Milestone 22

## Plan
- Three-way sync architecture: iOS EventKit ↔ BetterSelf Backend ↔ Google Calendar API
- Sync flow on app launch: pull from backend, merge with SwiftData, reconcile with EventKit, push local changes
- AI-created events flow from backend to user's chosen calendar (Apple or Google)
- Conflict resolution using last-modified timestamp with user prompt for close ties
- Background sync via BGTaskScheduler (every 15 min) and EKEventStoreChanged notification
- Calendar connection status in Settings with sync status, last sync time, manual sync button
- Handle edge cases: deleted events, recurring changes, timezone changes

## Key Files
| File | Description |
|------|-------------|
| CalendarSyncEngine.swift | Sync orchestration, conflict resolution (update) |
| CalendarService.swift | API communication, EventKit integration (update) |
| CalendarViewModel.swift | UI state, sync triggers (update) |

## Implementation Details

1. **Three-way sync architecture**: iOS EventKit (Apple Calendar) ↔ BetterSelf Backend ↔ Google Calendar API. The backend acts as the source of truth for AI-created events.

2. **Sync flow on app launch**:
   - a) Pull events from backend (GET /calendar/events)
   - b) Merge with local SwiftData cache
   - c) Reconcile with EventKit events
   - d) Push any local-only changes to backend (POST /calendar/sync)

3. **AI-created events**: When AI creates an event via backend, it's stored in DynamoDB. On next sync, it appears in the app AND is written to the user's chosen calendar (Apple or Google) via EventKit or Google Calendar API.

4. **Conflict resolution strategy**: For same event modified in multiple places, use last-modified timestamp. If timestamps are within 1 minute, prompt user to choose version.

5. **Background sync**: BGTaskScheduler runs sync every 15 minutes, EKEventStoreChanged notification triggers immediate sync.

6. **Calendar connection status in Settings**: Show sync status, last sync time, error indicators, manual "Sync Now" button.

7. **Edge cases**: Handle deleted events, changed recurring events, timezone changes.

## Testing
- Events from Apple Calendar appear in app after sync
- AI-created events appear in Apple/Google Calendar
- Edits in external calendar reflected in app
- Conflict resolution prompts work
- Background sync runs as scheduled
- Deleted events handled correctly

## Test Requirements (Definition of Done)
- Integration test for full sync round-trip: create event on backend → sync to iOS → verify in SwiftData
- Integration test for conflict scenarios (same event modified locally and remotely, timestamp tie-breaking)
- Unit tests for three-way merge logic (new/updated/deleted from each source)
- Unit test for AI-created event propagation (backend → SwiftData → EventKit)
- Edge case tests: deleted events, recurring event modifications, timezone change handling

## Notes
Duration: 3 days
