# Milestone 19: Tasks & Habits API

## Status
Not Started

## Goal
Implement task management with smart prioritization and habit tracking with streak calculation. Tasks support full CRUD with due dates and priorities; habits track daily/weekly frequency with consecutive completion streaks.

## Dependencies
Milestones 11 (Database Setup), 12 (Lambda API), 14 (User & Auth API)

## Plan
- Implement Tasks API with CRUD and prioritization endpoint
- Implement Habits API with check-in and streak calculation
- Add habits summary endpoint
- Store tasks and habits in DynamoDB

## Key Files
| File | Description |
|------|-------------|
| api/routers/tasks.py | Task CRUD and prioritization endpoints |
| api/routers/habits.py | Habit CRUD, check-in, summary endpoints |
| api/models/tasks.py | Task Pydantic models |
| api/models/habits.py | Habit Pydantic models |

## Implementation Details

1. **Tasks API**:
   - POST /tasks: Create task (title, priority, due_date, description)
   - GET /tasks: List with filters (status, priority, date range)
   - GET /tasks/{id}: Get task detail
   - PUT /tasks/{id}: Update task
   - DELETE /tasks/{id}: Delete task
   - PUT /tasks/{id}/complete: Mark completed with timestamp

2. **GET /tasks/prioritized**: AI-enhanced prioritization — calls Bedrock to rank tasks by urgency + importance matrix, considers due dates, dependencies, and user's schedule

3. **Habits API**:
   - POST /habits: Create habit (name, frequency: daily/weekly, target_count)
   - GET /habits: List all with current streak
   - PUT /habits/{id}: Update habit
   - DELETE /habits/{id}: Delete habit
   - POST /habits/{id}/check-in: Record completion for today

4. **Streak calculation**: Consecutive days/weeks of check-ins, reset on miss, stored in habit record, recalculated on check-in

5. **GET /habits/summary**: Today's habits due, completion status, longest streaks

6. **Storage**: Tasks in DynamoDB Tasks table (with status-due-index and priority-index GSIs for filtered queries), habits in DynamoDB Habits table (with streak counter)

## Testing
- Task CRUD works
- Prioritization returns sensible ordering
- Habit check-in increments streak
- Missed day resets streak
- Summary endpoint is accurate
- Filters work correctly

## Test Requirements (Definition of Done)
- pytest tests for task CRUD and filter combinations (status, priority, date range)
- pytest tests for prioritization logic (urgency × importance ordering, due-date weighting)
- pytest tests for streak calculation (consecutive check-ins increment, missed day resets, edge: first check-in)
- pytest tests for habit check-in idempotency (double check-in same day)
- pytest tests for /habits/summary accuracy (due today, completion status, longest streak)

## Notes
- **Duration**: 2 days
