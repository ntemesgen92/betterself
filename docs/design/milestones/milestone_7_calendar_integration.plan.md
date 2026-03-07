# Milestone 7: Calendar Integration

## Status
Not Started

## Goal
Integrate EventKit for Apple Calendar and Google Calendar REST API. Implement a bidirectional sync engine that merges events from both sources with deduplication and conflict resolution. Connect to the Calendar UI built in Milestone 6.

## Dependencies
- Milestone 2 (Data Models & Local Storage)
- Milestone 6 (Calendar UI)

## Plan
- EventKitManager: Apple Calendar access and CRUD
- GoogleCalendarManager: OAuth, Calendar API v3, event CRUD
- CalendarSyncEngine: merge, deduplication, conflict resolution, background sync
- CalendarService: unified facade over both managers
- Settings integration for calendar connection and re-auth

## Key Files
| File | Description |
|------|-------------|
| CalendarService.swift | Unified facade for all calendar operations |
| EventKitManager.swift | EventKit/EKEventStore integration |
| GoogleCalendarManager.swift | Google Sign-In, Calendar API v3 |
| CalendarSyncEngine.swift | Sync logic, merge, conflict resolution |

## Implementation Details

1. **EventKitManager**
   - Request calendar access (`EKAuthorizationStatus`)
   - Fetch events from EKEventStore with date range predicate
   - Create, update, delete events via EKEventStore
   - Map EKEvent to app CalendarEvent model (including external_id)
   - Handle EKRecurrenceRule for recurring events
   - Observe EKEventStore changes for reactive updates

2. **GoogleCalendarManager**
   - Implement Google Sign-In for OAuth 2.0
   - Use Google Calendar REST API v3 for events
   - List events with pagination and syncToken for incremental sync
   - Create, update, delete events
   - Map Google event JSON to CalendarEvent model
   - Store refresh tokens in KeychainManager

3. **CalendarSyncEngine**
   - Merge events from EventKit and Google Calendar
   - Deduplication: match by external_id (e.g., Google event ID, EKEvent eventIdentifier)
   - Conflict resolution: last-modified-wins or prompt user for significant conflicts
   - Periodic background sync using BGTaskScheduler
   - Update local SwiftData/ModelContext with synced events
   - Emit sync status for UI (syncing, last synced, error)

4. **CalendarService Facade**
   - Single interface: fetchEvents(from:to:), createEvent, updateEvent, deleteEvent
   - Routes to EventKitManager or GoogleCalendarManager based on event source
   - For create: user selects source (Apple or Google)
   - Maps external events to app CalendarEvent model consistently

5. **Settings Integration**
   - Calendar connection screen: toggle Apple Calendar on/off
   - Google Calendar: connect/disconnect, re-auth flow
   - Display connection status and last sync time
   - Handle auth errors (token expired, revoked)

## Testing
- Apple Calendar events appear in app after permission grant
- Google Calendar OAuth flow completes and stores tokens
- Events created in app appear in source calendar (Apple and Google)
- Sync detects and resolves conflicts (last-modified test cases)
- Background sync runs and updates data
- Re-auth flow works when token expires

## Test Requirements (Definition of Done)
- Unit tests for CalendarSyncEngine conflict resolution (last-modified-wins, same-timestamp tie)
- Unit tests for event deduplication by external_id across sources
- Unit tests for merge logic (new, updated, deleted events from each source)
- CalendarService facade routing tests (Apple vs Google source dispatch)
- Mock-based tests for EventKitManager and GoogleCalendarManager mapping

## Notes
- Google Calendar API requires Google Cloud Console project setup
- Start OAuth consent screen verification early for production
- Duration: 4 days
