# Milestone 2: Data Models & Local Storage

## Status
Not Started

## Goal
Define all SwiftData models for the app's core entities, create a mock data service for development and prototyping, and implement the repository pattern for clean data access abstraction.

## Dependencies
- Milestone 1 (Project Setup)

## Plan
- Define SwiftData @Model classes for User, BlockingProfile, CalendarEvent, Task, Habit, AIConversation, DailyBriefing
- Configure SwiftData ModelContainer with schema migrations
- Create MockDataService with sample data for all entities
- Implement repository pattern (protocols + implementations) for each entity
- Add KeychainManager for secure token storage using KeychainAccess

## Key Files
| File | Description |
|------|-------------|
| User.swift | User profile model |
| BlockingProfile.swift | Focus/blocking profile configuration |
| CalendarEvent.swift | Calendar event entity |
| Task.swift | Task/todo model |
| Habit.swift | Habit tracking model |
| AIConversation.swift | AI chat conversation and messages |
| DailyBriefing.swift | Daily briefing summary model |
| SwiftDataContainer.swift | ModelContainer configuration |
| MockDataService.swift | Sample data for development |

## Implementation Details

1. **SwiftData Models**
   - Define `@Model` classes for all entities with appropriate properties
   - User: id, name, email, preferences
   - BlockingProfile: name, icon, mode (Timed/Cold Turkey/Allowlist), schedule, strict mode, app selections
   - BlockingSession: profile reference, start/end times, completion status
   - CalendarEvent: title, start/end date, location, description, source (Apple/Google/AI), external_id
   - Task: title, due date, completed, priority
   - Habit: name, streak count, last completed date
   - AIConversation: messages array, created/updated dates
   - DailyBriefing: date, summary text, highlights

2. **ModelContainer Configuration**
   - Create shared ModelContainer with all model types
   - Configure schema with versioning for future migrations
   - Set up ModelContext injection points

3. **MockDataService**
   - 5 sample blocking profiles (e.g., Work Focus, Deep Work, Social Media Block)
   - 10 calendar events across various dates
   - 8 tasks with mixed completion states
   - 4 habits with streak data
   - Sample AI conversations with varied message types

4. **Repository Pattern**
   - Define protocols: UserRepository, BlockingProfileRepository, CalendarEventRepository, etc.
   - Implement concrete repositories that wrap SwiftData ModelContext
   - Use protocol injection for testability and mock swapping

5. **KeychainManager**
   - Wrap KeychainAccess for OAuth tokens (Google, future API keys)
   - Methods: save, load, delete for key-value pairs
   - Handle migration of tokens on app update

## Testing
- Unit tests for model creation and validation
- MockDataService returns expected data counts and structure
- SwiftData persistence round-trip tests (save, fetch, verify)
- KeychainManager stores and retrieves tokens correctly

## Notes
- Duration: 2 days
