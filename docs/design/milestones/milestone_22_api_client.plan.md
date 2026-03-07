# Milestone 22: API Client & Sync

## Status
Not Started

## Goal
Build the Swift API client layer that communicates with the backend, with offline queue support, background sync, and error handling. Supports graceful degradation when offline and transparent retry on connectivity restore.

## Dependencies
Milestones 12 (Lambda API), 21 (Auth Integration)

## Plan
- Create generic APIClient with token injection and retry logic
- Implement typed API methods (UserAPI, BlockingAPI, CalendarAPI, etc.)
- Add NetworkMonitor and OfflineQueue
- Build SyncEngine for background sync and conflict resolution
- Add error handling UI (banners, offline indicator, retry)

## Key Files
| File | Description |
|------|-------------|
| APIClient.swift | HTTP client, token injection, JSON encoding, retry |
| SyncEngine.swift | Background sync, offline queue replay, conflict resolution |
| OfflineQueue.swift | Queue write operations when offline |
| NetworkMonitor.swift | NWPathMonitor wrapper, connectivity status |

## Implementation Details

1. **APIClient**: Generic HTTP client using URLSession (or Alamofire), base URL configuration, automatic token injection from AuthService, JSON encoding/decoding with Codable, error handling (map HTTP errors to app error types), request retry with exponential backoff

2. **Typed API methods**: UserAPI, BlockingAPI, CalendarAPI, AIAPI, TaskAPI, HabitAPI (each maps to backend router endpoints)

3. **NetworkMonitor**: Wraps NWPathMonitor, publishes connectivity status

4. **OfflineQueue**: When offline, queue write operations (create, update, delete) to SwiftData

5. **SyncEngine**: On connectivity restore, replay offline queue in order; handle conflicts (server wins by default, prompt user for ambiguous cases); periodic background sync via BGTaskScheduler (sync blocking sessions, calendar events, habit check-ins)

6. **Error handling UI**: Show inline error banners, offline indicator in nav bar, retry buttons on failed operations

## Testing
- API calls succeed with valid token
- 401 triggers token refresh
- Offline operations queued and replayed on reconnect
- Background sync runs periodically
- Error states display correctly in UI

## Test Requirements (Definition of Done)
- Unit tests for OfflineQueue replay (operations replayed in order on reconnect, queue cleared after success)
- Unit tests for retry logic (exponential backoff timing, max retry cap, non-retryable error short-circuit)
- Unit tests for APIClient token injection and 401 → token refresh flow
- Unit tests for NetworkMonitor connectivity state transitions
- Unit tests for SyncEngine conflict resolution (server-wins default, ambiguous case detection)

## Notes
- **Duration**: 3 days
