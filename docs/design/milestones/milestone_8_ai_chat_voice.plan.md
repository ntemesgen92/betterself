# Milestone 8: AI Chat UI & Voice

## Status
Not Started

## Goal
Build the AI chat interface with push-to-talk voice input using Apple Speech framework, conversation history display, and voice waveform animation. Connect to mock AI responses for development; backend integration comes later.

## Dependencies
- Milestone 1 (Project Setup)
- Milestone 2 (Data Models & Local Storage)
- Milestone 3 (Tab Navigation & Home Dashboard)

## Plan
- AIChatView: conversation UI with message bubbles, text input, mic button
- VoiceInputView: tap-to-record with pulsing mic
- SpeechService: SFSpeechRecognizer for on-device speech-to-text
- VoiceWaveformView: animated bars during recording and playback
- MessageBubble: text, action cards, loading indicator
- AIChatViewModel: conversation state, mock AI, voice state
- Persist conversations in SwiftData

## Key Files
| File | Description |
|------|-------------|
| AIChatView.swift | Main chat interface |
| AIChatViewModel.swift | Conversation and voice state |
| VoiceInputView.swift | Push-to-talk mic button |
| MessageBubble.swift | Message display (text, cards, loading) |
| SpeechService.swift | Speech recognition wrapper |
| VoiceWaveformView.swift | Waveform animation |

## Implementation Details

1. **AIChatView**
   - ScrollView/List of message bubbles
   - User messages on right (blue bubble), AI on left (gray bubble)
   - Text input bar at bottom with send button
   - Mic button (replaces or supplements text input when voice active)
   - Action confirmation cards inline (e.g., "Schedule gym at 6pm?" with Confirm/Cancel)

2. **VoiceInputView**
   - Large circular mic button
   - Tap to start recording; tap again to stop
   - Pulse animation when recording active
   - Visual feedback: recording state, processing state

3. **SpeechService**
   - Wrap Apple SFSpeechRecognizer for on-device speech-to-text
   - Request speech recognition authorization
   - Real-time transcription as user speaks (partial results)
   - Language detection or user-selectable locale
   - Handle errors: denied, unavailable, no speech
   - Return final transcript on stop

4. **VoiceWaveformView**
   - Animated bars or wave during recording
   - Uses AudioEngine metering levels for amplitude
   - During AI speech playback: drive from audio level (future)
   - Smooth animations, low CPU impact

5. **MessageBubble**
   - Text content with appropriate styling
   - Action cards: title, optional subtitle, Confirm and Cancel buttons
   - Loading indicator (typing dots or skeleton) for AI thinking
   - Timestamp optional
   - Support for long messages with truncation/expand

6. **AIChatViewModel**
   - Manages conversation (messages array) with @Observable
   - Sends user messages to mock AI service (no backend yet)
   - Handles voice recording: start → transcribe → send
   - Mock AI responses for development:
     - "schedule [X] at [time]" → action card confirmation
     - "block [app]" → action card
     - "give me my briefing" → canned briefing summary
     - Default: generic "I'm your AI assistant" response
   - Persists conversations in SwiftData (AIConversation model)
   - Load existing conversation on open

7. **Navigation**
   - Accessible from Home quick action "Talk to AI"
   - Modal or push to AIChatView
   - Back button returns to previous screen

## Testing
- Voice recording starts and stops on tap
- Speech transcribes correctly (test with clear speech)
- Waveform animates during recording
- Messages display in correct bubbles (user/AI)
- Action cards render with functional Confirm/Cancel
- Mock AI responds to canned commands (schedule, block, briefing)
- Conversation persists after app restart
- Loading state shows while "AI" is "thinking"

## Notes
- Duration: 4 days
