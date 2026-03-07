# BetterSelf -- API Contract

> **Status:** Draft -- to be finalized at Sync Point 2 (End of Week 3)
>
> Both developers must sign off on any changes to this document. Update the "Last Updated" date and note the change.
>
> **Last Updated:** TBD
> **Signed Off:** Dev A [ ] / Dev B [ ]

## Base Configuration

- **Base URL (staging):** `https://api-staging.betterself.app/v1`
- **Base URL (prod):** `https://api.betterself.app/v1`
- **Auth:** All endpoints (except health) require `Authorization: Bearer <cognito-jwt>` header
- **Content-Type:** `application/json`
- **Rate Limiting:** 100 req/min per user (free), 500 req/min (premium)

## Error Response Format

All errors follow this shape:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": {}
  }
}
```

Standard error codes:
- `400` -- VALIDATION_ERROR, INVALID_REQUEST
- `401` -- UNAUTHORIZED, TOKEN_EXPIRED
- `403` -- FORBIDDEN, PREMIUM_REQUIRED, RATE_LIMITED
- `404` -- NOT_FOUND
- `409` -- CONFLICT
- `500` -- INTERNAL_ERROR

---

## Health

### GET /health

No auth required.

```json
// Response 200
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2026-03-04T12:00:00Z"
}
```

---

## Auth & Users

### POST /auth/register

Called after Cognito sign-up confirmation to create the app-level user record.

```json
// Request
{
  "name": "Abel",
  "timezone": "America/New_York",
  "onboarding_data": {
    "goals": ["reduce_screen_time", "better_schedule"],
    "productive_hours": "morning",
    "work_days": ["mon", "tue", "wed", "thu", "fri"],
    "work_start": "09:00",
    "work_end": "17:00"
  }
}

// Response 201
{
  "id": "usr_abc123",
  "email": "abel@example.com",
  "name": "Abel",
  "subscription_tier": "free",
  "ai_queries_remaining": 10,
  "created_at": "2026-03-04T12:00:00Z"
}
```

### GET /users/me

```json
// Response 200
{
  "id": "usr_abc123",
  "email": "abel@example.com",
  "name": "Abel",
  "subscription_tier": "free",
  "ai_queries_remaining": 7,
  "preferences": {
    "timezone": "America/New_York",
    "notification_daily_briefing": true,
    "notification_focus_reminders": true,
    "notification_schedule_alerts": true,
    "voice_quality": "standard",
    "productive_hours": "morning"
  },
  "created_at": "2026-03-04T12:00:00Z"
}
```

### PUT /users/me

```json
// Request (partial update)
{
  "name": "Abel S.",
  "preferences": {
    "voice_quality": "premium",
    "notification_daily_briefing": false
  }
}

// Response 200
{ /* full user object */ }
```

### DELETE /users/me

```json
// Response 204 (no body)
// Deletes all user data (GDPR compliance)
```

---

## Blocking Profiles

### POST /blocking/profiles

```json
// Request
{
  "name": "Work Focus",
  "mode": "timed",
  "blocked_apps": ["com.instagram.ios", "com.twitter.ios"],
  "blocked_categories": ["social_networking", "games"],
  "allowed_apps": [],
  "schedule": {
    "days": ["mon", "tue", "wed", "thu", "fri"],
    "start_time": "09:00",
    "end_time": "17:00"
  },
  "strict_mode": true
}

// Response 201
{
  "id": "prof_xyz789",
  "user_id": "usr_abc123",
  "name": "Work Focus",
  "mode": "timed",
  "blocked_apps": ["com.instagram.ios", "com.twitter.ios"],
  "blocked_categories": ["social_networking", "games"],
  "allowed_apps": [],
  "schedule": { /* ... */ },
  "strict_mode": true,
  "is_active": false,
  "created_at": "2026-03-04T12:00:00Z",
  "updated_at": "2026-03-04T12:00:00Z"
}
```

### GET /blocking/profiles

```json
// Response 200
{
  "profiles": [ /* array of profile objects */ ],
  "count": 3
}
```

### GET /blocking/profiles/{id}

### PUT /blocking/profiles/{id}

### DELETE /blocking/profiles/{id}

### POST /blocking/sessions

Log a completed (or overridden) focus session.

```json
// Request
{
  "profile_id": "prof_xyz789",
  "start_time": "2026-03-04T09:00:00Z",
  "end_time": "2026-03-04T11:30:00Z",
  "override_attempts": 2,
  "completed": true
}

// Response 201
{
  "id": "sess_abc456",
  /* full session object */
}
```

### GET /blocking/sessions?start_date=2026-03-01&end_date=2026-03-07

### GET /blocking/stats

```json
// Response 200
{
  "today": {
    "total_focus_minutes": 150,
    "sessions_completed": 2,
    "sessions_overridden": 0,
    "blocked_attempts": 12
  },
  "week": {
    "total_focus_minutes": 720,
    "sessions_completed": 8,
    "completion_rate": 0.89,
    "avg_session_minutes": 90
  },
  "month": {
    "total_focus_minutes": 3200,
    "sessions_completed": 35,
    "completion_rate": 0.85
  }
}
```

---

## Calendar Events

### POST /calendar/events

```json
// Request
{
  "title": "Team Standup",
  "start_time": "2026-03-05T10:00:00Z",
  "end_time": "2026-03-05T10:30:00Z",
  "location": "Zoom",
  "description": "Daily sync",
  "source": "betterself",
  "recurrence": {
    "rule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
    "end_date": "2026-06-01"
  }
}

// Response 201
{
  "id": "evt_def789",
  "user_id": "usr_abc123",
  "external_id": null,
  "source": "betterself",
  "title": "Team Standup",
  "start_time": "2026-03-05T10:00:00Z",
  "end_time": "2026-03-05T10:30:00Z",
  "location": "Zoom",
  "description": "Daily sync",
  "ai_created": false,
  "recurrence": { /* ... */ },
  "created_at": "2026-03-04T12:00:00Z"
}
```

### GET /calendar/events?start_date=2026-03-01&end_date=2026-03-31&source=all

### GET /calendar/events/{id}

### PUT /calendar/events/{id}

### DELETE /calendar/events/{id}

### POST /calendar/sync

Batch sync from iOS client. Sends local changes, receives server changes.

```json
// Request
{
  "last_sync_at": "2026-03-04T10:00:00Z",
  "local_changes": [
    { "action": "create", "event": { /* event object */ } },
    { "action": "update", "id": "evt_def789", "event": { /* partial */ } },
    { "action": "delete", "id": "evt_old123" }
  ]
}

// Response 200
{
  "server_changes": [
    { "action": "create", "event": { /* new event from AI or other source */ } },
    { "action": "update", "event": { /* updated event */ } }
  ],
  "conflicts": [
    {
      "event_id": "evt_def789",
      "local_version": { /* ... */ },
      "server_version": { /* ... */ },
      "resolution": "server_wins"
    }
  ],
  "sync_timestamp": "2026-03-04T12:00:00Z"
}
```

### GET /calendar/conflicts?start_date=2026-03-05&end_date=2026-03-05

```json
// Response 200
{
  "conflicts": [
    {
      "event_a": { "id": "evt_1", "title": "Meeting", "start_time": "10:00", "end_time": "11:00" },
      "event_b": { "id": "evt_2", "title": "Gym", "start_time": "10:30", "end_time": "11:30" },
      "overlap_minutes": 30
    }
  ]
}
```

---

## AI Secretary

### POST /ai/chat

```json
// Request
{
  "message": "Schedule gym 3 times this week in the evening"
}

// Response 200
{
  "id": "msg_ghi012",
  "conversation_id": "conv_xyz",
  "text": "I'll schedule gym sessions for you this week. Here's what I suggest:\n- Tuesday 6:00-7:00 PM\n- Thursday 6:00-7:00 PM\n- Saturday 10:00-11:00 AM\n\nShall I go ahead and add these to your calendar?",
  "action": {
    "type": "create_events",
    "status": "pending_confirmation",
    "params": {
      "events": [
        { "title": "Gym", "start_time": "2026-03-05T18:00:00Z", "end_time": "2026-03-05T19:00:00Z" },
        { "title": "Gym", "start_time": "2026-03-07T18:00:00Z", "end_time": "2026-03-07T19:00:00Z" },
        { "title": "Gym", "start_time": "2026-03-09T10:00:00Z", "end_time": "2026-03-09T11:00:00Z" }
      ]
    }
  },
  "tokens_used": 450,
  "queries_remaining": 6
}
```

### POST /ai/actions/{id}/confirm

```json
// Response 200
{
  "status": "executed",
  "results": [
    { "type": "event_created", "event_id": "evt_new1" },
    { "type": "event_created", "event_id": "evt_new2" },
    { "type": "event_created", "event_id": "evt_new3" }
  ]
}
```

### POST /ai/actions/{id}/reject

```json
// Response 200
{
  "status": "rejected",
  "text": "No problem! Let me know if you'd like different times."
}
```

### GET /ai/conversations?limit=20&offset=0

```json
// Response 200
{
  "messages": [
    {
      "id": "msg_001",
      "role": "user",
      "content": "Schedule gym 3 times this week",
      "timestamp": "2026-03-04T12:00:00Z"
    },
    {
      "id": "msg_002",
      "role": "assistant",
      "content": "I'll schedule gym sessions...",
      "action": { /* ... */ },
      "timestamp": "2026-03-04T12:00:01Z"
    }
  ],
  "total": 42,
  "has_more": true
}
```

### POST /ai/briefing

Generate (or regenerate) today's briefing.

```json
// Response 200
{
  "id": "brief_today",
  "date": "2026-03-04",
  "schedule_summary": {
    "total_events": 5,
    "first_event": { "title": "Standup", "time": "10:00" },
    "busy_hours": 4,
    "free_blocks": [
      { "start": "08:00", "end": "10:00", "label": "Deep work opportunity" },
      { "start": "14:00", "end": "16:00", "label": "Afternoon focus block" }
    ]
  },
  "tasks_summary": {
    "total_pending": 8,
    "top_3": [
      { "id": "task_1", "title": "Finish report", "priority": "high", "due": "2026-03-05" },
      { "id": "task_2", "title": "Review PR #42", "priority": "medium", "due": "2026-03-04" },
      { "id": "task_3", "title": "Prepare slides", "priority": "medium", "due": "2026-03-06" }
    ]
  },
  "habits_summary": {
    "due_today": ["Meditate", "Read 30 min", "Exercise"],
    "completed_today": ["Meditate"],
    "current_streaks": { "Meditate": 12, "Read 30 min": 5, "Exercise": 3 }
  },
  "focus_recommendation": "You have a 2-hour free block from 8-10 AM. I'd suggest a deep work session to finish the report.",
  "ai_insight": "You've been most productive before noon this week. I've kept your mornings clear."
}
```

### GET /ai/briefing/today

Returns cached briefing if already generated today.

---

## Voice Processing (Premium Only)

### POST /voice/process

Multipart form upload.

```
Content-Type: multipart/form-data

Fields:
  audio: <binary WAV/M4A file>
  format: "wav" | "m4a"
```

```json
// Response 200
{
  "transcript": "Schedule a meeting with Sarah tomorrow at 2pm",
  "ai_response": {
    "text": "I'll schedule a meeting with Sarah tomorrow at 2:00 PM. Shall I add it?",
    "action": { "type": "create_event", "status": "pending_confirmation", /* ... */ }
  },
  "audio_url": "https://s3.../response_audio.mp3",
  "audio_expires_at": "2026-03-04T13:00:00Z"
}
```

### POST /voice/speak

Text-to-speech only.

```json
// Request
{ "text": "Your next meeting is in 30 minutes with the marketing team." }

// Response 200
{
  "audio_url": "https://s3.../speech.mp3",
  "audio_expires_at": "2026-03-04T13:00:00Z"
}
```

---

## Tasks

### POST /tasks

```json
// Request
{
  "title": "Finish quarterly report",
  "priority": "high",
  "due_date": "2026-03-07T17:00:00Z",
  "description": "Include Q1 sales numbers"
}

// Response 201
{
  "id": "task_jkl345",
  "user_id": "usr_abc123",
  "title": "Finish quarterly report",
  "priority": "high",
  "status": "pending",
  "due_date": "2026-03-07T17:00:00Z",
  "description": "Include Q1 sales numbers",
  "completed_at": null,
  "created_at": "2026-03-04T12:00:00Z"
}
```

### GET /tasks?status=pending&priority=high

### GET /tasks/{id}

### PUT /tasks/{id}

### PUT /tasks/{id}/complete

### DELETE /tasks/{id}

### GET /tasks/prioritized

AI-ranked task list.

```json
// Response 200
{
  "tasks": [ /* tasks ordered by AI priority score */ ],
  "reasoning": "Report is due tomorrow and marked high priority. PR review has same-day deadline."
}
```

---

## Habits

### POST /habits

```json
// Request
{
  "name": "Meditate",
  "frequency": "daily",
  "target_count": 1
}

// Response 201
{
  "id": "hab_mno678",
  "user_id": "usr_abc123",
  "name": "Meditate",
  "frequency": "daily",
  "target_count": 1,
  "current_streak": 0,
  "longest_streak": 0,
  "created_at": "2026-03-04T12:00:00Z"
}
```

### GET /habits

### PUT /habits/{id}

### DELETE /habits/{id}

### POST /habits/{id}/check-in

```json
// Response 200
{
  "id": "hab_mno678",
  "name": "Meditate",
  "current_streak": 13,
  "longest_streak": 13,
  "checked_in_today": true,
  "last_check_in": "2026-03-04T08:30:00Z"
}
```

### GET /habits/summary

```json
// Response 200
{
  "due_today": [
    { "id": "hab_mno678", "name": "Meditate", "checked_in_today": true, "current_streak": 13 },
    { "id": "hab_pqr901", "name": "Read 30 min", "checked_in_today": false, "current_streak": 5 }
  ],
  "completion_rate_week": 0.85
}
```

---

## Notifications

### POST /notifications/register

```json
// Request
{
  "device_token": "<apns-device-token>",
  "platform": "ios"
}

// Response 200
{
  "endpoint_arn": "arn:aws:sns:...",
  "registered": true
}
```

### PUT /notifications/preferences

```json
// Request
{
  "daily_briefing": true,
  "daily_briefing_time": "07:00",
  "focus_reminders": true,
  "focus_reminder_minutes_before": 15,
  "schedule_alerts": true,
  "schedule_alert_minutes_before": 10,
  "ai_nudges": false
}

// Response 200
{ /* updated preferences */ }
```
