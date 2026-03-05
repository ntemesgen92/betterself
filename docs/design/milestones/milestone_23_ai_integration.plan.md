# Milestone 23: AI Integration (iOS)

## Status
Not Started

## Goal
Connect the iOS voice chat UI to the backend AI secretary, implement streaming responses, and wire up the action confirmation flow. Supports both free tier (Apple Speech + text response) and premium (full voice-to-voice pipeline).

## Dependencies
Milestones 8 (AI Chat & Voice UI), 17 (AI Secretary API), 18 (Voice API), 22 (API Client & Sync)

## Plan
- Create AIService wrapping backend AI endpoints
- Update AIChatViewModel to use real backend
- Implement voice flows for free and premium tiers
- Add streaming responses with progressive text reveal
- Build ActionConfirmationCard for action confirm/reject
- Handle AI errors gracefully

## Key Files
| File | Description |
|------|-------------|
| AIService.swift | Wraps /ai/chat, /ai/conversations, /ai/actions, /voice/process |
| AIChatViewModel.swift | Use real AIService, display action confirmations |
| VoiceInputView.swift | Voice input handling (update) |
| ActionConfirmationCard.swift | Confirm/Reject UI for proposed actions |

## Implementation Details

1. **AIService**: Wraps API calls to /ai/chat, /ai/conversations, /ai/actions/confirm, /ai/actions/reject, /voice/process

2. **Update AIChatViewModel**: Use real AIService instead of mock — send user text/voice to backend, receive AI response, display action confirmations

3. **Voice flow (free tier)**: User taps mic → Apple Speech transcribes on-device → text sent to /ai/chat → response displayed as text + spoken via AVSpeechSynthesizer

4. **Voice flow (premium)**: User taps mic → audio recorded → sent to /voice/process → receives audio response + text + action → plays audio response via AVAudioPlayer

5. **Streaming responses**: Use Server-Sent Events or chunked transfer encoding from /ai/chat to show AI response as it generates (typing indicator then progressive text reveal)

6. **Action confirmation flow**: AI proposes action (e.g., "Schedule gym at 6pm") → ActionConfirmationCard renders with details + Confirm/Reject buttons → user taps Confirm → calls /ai/actions/{id}/confirm → action executes → success feedback shown

7. **Error handling**: Timeout, rate limit reached (free tier), model unavailable — handle gracefully

## Testing
- Text chat works end-to-end with backend
- Voice input transcribes and gets AI response
- Premium voice returns audio
- Action confirmations execute correctly
- Streaming renders progressively
- Error states handled

## Notes
- **Duration**: 3 days
