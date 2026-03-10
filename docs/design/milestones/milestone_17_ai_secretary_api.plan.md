# Milestone 17: AI Secretary API

## Status
Not Started

## Goal
Implement the core AI secretary conversation endpoint with natural language understanding, calendar action execution, schedule optimization, and daily briefing generation. The AI acts as a professional executive assistant that responds concisely, proposes actions as structured JSON, and asks for confirmation before making changes.

## Dependencies
Milestones 13 (AI & Voice Services), 14 (User & Auth API), 16 (Calendar API)

## Plan
- Implement chat endpoint with context-aware AI responses
- Add conversation history and action confirmation endpoints
- Build daily briefing generation and retrieval
- Implement system prompt engineering and context window management
- Add token budgeting for free tier limits

## Key Files
| File | Description |
|------|-------------|
| api/routers/ai.py | AI chat, conversations, actions, briefing endpoints |
| api/models/ai.py | Pydantic models for AI request/response |
| api/services/ai_service.py | Bedrock invocation, context building, action execution |
| api/prompts/secretary_system_prompt.txt | System prompt for AI secretary persona |

## Implementation Details

1. **POST /ai/chat**: Accepts user message (text), returns AI response with optional action.
   - Flow: receive message → build context (recent conversations, today's schedule, tasks, habits) → invoke Bedrock with system prompt + context + user message → parse response for actions → execute actions (create event, create task, update blocking profile, etc.) → return response text + action confirmation

2. **GET /ai/conversations**: List conversation history with pagination

3. **POST /ai/actions/{id}/confirm**: User confirms a proposed action (e.g., scheduling an event), executes the action

4. **POST /ai/actions/{id}/reject**: User rejects a proposed action

5. **POST /ai/briefing**: Generate daily briefing for the user. Aggregates: today's events, pending tasks ranked by priority, habit check-ins due, focus session recommendations based on schedule gaps, AI insights from usage patterns

6. **GET /ai/briefing/today**: Retrieve today's briefing

7. **System prompt engineering**: The AI is a professional executive assistant. It responds concisely, proposes actions as structured JSON, asks for confirmation before making changes, understands schedule conflicts, can suggest optimal times for activities

8. **Context window management**: Include last 10 conversation turns + today's schedule + active tasks in each request to maintain continuity

9. **Token budgeting**: Track tokens per user per day, enforce free tier limits (10 queries/day)

## Testing
- Chat endpoint returns coherent responses with correct action structures
- Actions execute correctly when confirmed
- Daily briefing aggregates data correctly
- Token budgeting enforces limits
- Conversation history is maintained

## Test Requirements (Definition of Done)
- pytest tests for action JSON parsing from AI response (valid actions, malformed, unsupported action types)
- pytest tests for context building (conversation history truncation, schedule inclusion, token budget)
- pytest tests for token budgeting and free-tier limit enforcement (10 queries/day, reset logic)
- pytest tests for conversation threading (history maintained across turns, pagination)
- pytest tests for action confirm/reject endpoints and side-effect execution

## Notes
- **Duration**: 4 days
