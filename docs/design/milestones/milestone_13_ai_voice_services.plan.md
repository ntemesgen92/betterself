# Milestone 13: AI & Voice Services Setup

## Status
Not Started

## Goal
Integrate AWS Bedrock for LLM capabilities and set up Transcribe + Polly for premium voice processing. Design prompt engineering for the AI secretary persona that produces structured actions alongside natural language responses.

## Dependencies
Milestones 9 (CDK Foundation), 12 (Lambda & API Gateway)

## Plan
- Enable AWS Bedrock and request model access
- Create AI service with Bedrock client and action parsing
- Design AI secretary system prompt with structured output
- Implement voice service with Transcribe and Polly
- Add CDK resources for Bedrock, Transcribe, and Polly permissions

## Key Files
| File | Description |
|------|-------------|
| api/services/ai_service.py | Bedrock runtime client, invoke_model, streaming, action parsing |
| api/services/voice_service.py | Transcribe streaming, Polly TTS, audio format handling |
| api/prompts/secretary_system_prompt.txt | AI secretary persona and structured output examples |

## Implementation Details
1. **AWS Bedrock**: Enable in account, request model access (Claude 3 Sonnet or Haiku for cost efficiency)
2. **ai_service.py**: Bedrock runtime client, invoke_model wrapper, streaming response support, token counting and budget enforcement
3. **System prompt**: Professional and efficient persona, understands calendar/task/blocking domains, outputs structured JSON actions alongside natural language responses, includes examples of calendar scheduling, task creation, blocking profile management
4. **voice_service.py**: AWS Transcribe streaming for real-time speech-to-text (premium), Polly neural voices for text-to-speech (Joanna or Matthew), audio format handling (PCM/MP3)
5. **Action parsing**: AI response contains user-facing text AND structured action object (e.g., {"action": "create_event", "params": {"title": "Gym", "time": "18:00"}})
6. **CDK resources**: Bedrock permissions on Lambda role, Transcribe/Polly permissions, S3 bucket for audio temp storage

## Testing
- Bedrock invocation returns coherent responses
- System prompt produces correct action structures
- Transcribe converts sample audio to text
- Polly generates audio from text
- End-to-end: text in → AI response + action JSON out

## Test Requirements (Definition of Done)
- Unit tests for Bedrock invocation wrapper (request formatting, response deserialization, error handling)
- Unit tests for prompt assembly (system prompt + context + user message concatenation, token budget enforcement)
- Unit tests for action JSON parsing from AI response text (valid actions, malformed JSON, missing fields)
- Unit tests for token counting and budget limit enforcement
- Unit tests for voice_service audio format handling (PCM/MP3 conversion paths)

## Notes
- **Duration**: 3 days
- Bedrock model access may need to be requested and can take 1-2 days for approval
- Use Claude 3 Haiku for development (cheaper/faster), Claude 3 Sonnet for production
