# Milestone 18: Voice Processing API

## Status
Not Started

## Goal
Implement the end-to-end voice pipeline: audio upload → AWS Transcribe → LLM processing → AWS Polly → audio response. Enables premium users to speak to the AI and receive natural-sounding audio replies.

## Dependencies
Milestones 13 (AI & Voice Services), 17 (AI Secretary API)

## Plan
- Implement full voice processing endpoint (upload → transcribe → AI → speak)
- Add transcribe-only and speak-only endpoints
- Configure S3 for temp audio storage with lifecycle rules
- Implement premium gating for voice endpoints

## Key Files
| File | Description |
|------|-------------|
| api/routers/voice.py | Voice process, transcribe, speak endpoints |
| api/services/voice_service.py | Transcribe, Polly, S3 integration |

## Implementation Details

1. **POST /voice/process**: Accepts audio file (WAV/M4A), returns audio response + text transcript + action. Full pipeline:
   - a) Upload audio to S3 temp bucket
   - b) Start Transcribe job (or use streaming for real-time)
   - c) Get transcript text
   - d) Pass text to AI secretary endpoint (reuse /ai/chat logic)
   - e) Convert AI response text to speech via Polly (Neural engine, professional voice)
   - f) Return: audio URL (S3 presigned), transcript text, AI response text, action (if any)

2. **POST /voice/transcribe**: Transcribe-only endpoint (for when iOS uses Apple Speech but wants to send text directly)

3. **POST /voice/speak**: Text-to-speech only endpoint (for converting AI text responses to audio)

4. **Audio format handling**: Accept WAV, M4A, FLAC; output MP3 or PCM

5. **Optimize latency**: Use Transcribe streaming API instead of batch jobs, parallelize where possible, cache common Polly responses

6. **S3 lifecycle rule**: Auto-delete temp audio after 24 hours

7. **Premium gating**: These endpoints only available to premium users; free tier uses Apple Speech on-device

## Testing
- Audio upload transcribes correctly
- Full pipeline returns audio response in <5 seconds
- Polly generates natural-sounding speech
- Presigned URLs work
- Large audio files handled gracefully
- Premium gating works

## Notes
- **Duration**: 3 days
