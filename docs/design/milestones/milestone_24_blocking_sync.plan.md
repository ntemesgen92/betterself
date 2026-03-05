# Milestone 24: Blocking Sync (iOS)

## Status
Not Started

## Goal
Sync blocking profiles and focus sessions between the iOS app and backend, enabling analytics data upload and cross-device consistency. Profile changes and session logs flow bidirectionally with server-wins conflict resolution.

## Dependencies
Milestones 5 (Family Controls), 15 (Blocking API), 22 (API Client & Sync)

## Plan
- Create BlockingSyncManager for two-way profile sync
- Implement session logging to backend on completion
- Add stats sync for Focus Home display
- Use BGTaskScheduler for background upload of pending sessions
- Update FocusViewModel and FocusHomeView with synced stats

## Key Files
| File | Description |
|------|-------------|
| BlockingService.swift | Profile and session management (update) |
| BlockingSyncManager.swift | Two-way sync, session upload, stats fetch |

## Implementation Details

1. **BlockingSyncManager**: Manages two-way sync of blocking profiles between local SwiftData and backend DynamoDB

2. **Profile sync**: On profile create/update/delete locally, push to backend. On app launch, pull latest profiles from backend and merge with local

3. **Session logging**: When a focus session completes (or is overridden), send session data to backend POST /blocking/sessions (duration, profile used, completed status, override attempts)

4. **Stats sync**: Periodically fetch aggregated stats from GET /blocking/stats to display in Focus Home

5. **Conflict resolution**: Server state wins for profiles (last-write-wins with timestamp comparison)

6. **Background upload**: Use BGTaskScheduler to upload pending session logs even when app is backgrounded

7. **Update FocusViewModel and FocusHomeView**: Display synced stats (total focus time, completion rate, streaks)

## Testing
- Profile created on device appears in backend
- Profile changes from backend reflected locally
- Session logs upload after completion
- Stats display correctly
- Offline sessions queued and uploaded later

## Notes
- **Duration**: 2 days
