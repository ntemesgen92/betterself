# BetterSelf -- AI/ML Data Lifecycle

> **Author:** Dev A
> **Status:** Draft
> **Purpose:** Document the complete AI/ML lifecycle for BetterSelf's AI secretary, from data collection through monitoring. This demonstrates understanding of how AI-powered products work end-to-end.

---

## Lifecycle Overview

```
[User Action] -> [Data Collection] -> [Data Pipeline] -> [Model Inference] -> [Action Execution] -> [User Feedback] -> [Evaluation] -> [Iteration]
```

---

## 1. Data Collection

### What data feeds the AI?

| Data Source | Type | Collection Method | Storage |
|-------------|------|-------------------|---------|
| Calendar events | Structured | EventKit + Google Calendar API sync | Aurora PostgreSQL |
| Tasks and priorities | Structured | User input + AI-created | Aurora PostgreSQL |
| Habits and streaks | Structured | User check-ins | DynamoDB |
| Blocking profiles and sessions | Structured | FamilyControls + manual config | DynamoDB |
| Conversation history | Unstructured text | AI chat interactions | DynamoDB (90-day TTL) |
| User preferences | Structured | Onboarding + settings | DynamoDB |
| Voice audio | Unstructured audio | Push-to-talk recording | S3 (24-hour TTL, not persisted) |
| App usage patterns | Structured | DeviceActivity framework | Local only (privacy) |

### Data Privacy Considerations
- Voice audio is transcribed and immediately deleted -- we do NOT store raw audio long-term
- App usage data stays on-device -- we only send aggregated stats (total focus time, completion rate)
- Conversation history has a 90-day TTL -- older conversations are automatically deleted
- Users can delete all their data at any time (GDPR compliance)

---

## 2. Data Pipeline

### How data flows from user actions to the LLM context window

[Describe the pipeline: When a user sends a message to the AI, what happens step by step?]

**Context Building Pipeline:**
1. Receive user message (text or transcribed audio)
2. Fetch from DynamoDB: last 10 conversation messages, user preferences
3. Fetch from Aurora: today's calendar events, active tasks (sorted by priority), habits due today
4. Fetch from DynamoDB: active blocking profiles, current session status
5. Assemble context window: system prompt + user context + conversation history + current message
6. Estimated token budget: ~2000 tokens context + ~500 tokens user message = ~2500 input tokens

### Data Freshness
- Calendar events: synced every 15 minutes + on-demand
- Tasks: real-time (written directly to Aurora)
- Conversation history: real-time (written after each exchange)
- User preferences: cached locally, synced on change

---

## 3. Model Selection

### Why AWS Bedrock with Claude 3?

| Consideration | Claude 3 Sonnet (Bedrock) | GPT-4o (OpenAI) | Gemini Pro (Google) | Open Source (Llama 3) |
|---------------|---------------------------|-------------------|---------------------|----------------------|
| Quality | Excellent for structured output | Excellent overall | Good | Good, but less reliable structured output |
| Latency | ~2-3s | ~2-4s | ~1-2s | Depends on hosting |
| Cost per 1K tokens | ~$0.003 input / $0.015 output | ~$0.005 / $0.015 | ~$0.001 / $0.002 | Hosting costs |
| AWS Integration | Native (Bedrock) | External API call | External API call | Self-hosted on EC2/ECS |
| Data Privacy | Stays in AWS, no training on data | Data sent to OpenAI | Data sent to Google | Full control |
| Ops Overhead | Zero (managed service) | Low (API) | Low (API) | High (hosting, scaling) |

**Decision:** Bedrock + Claude 3 because:
- Native AWS integration (our infra is all AWS)
- Strong structured JSON output (needed for action parsing)
- Data stays within our AWS account (privacy advantage for users)
- No model hosting overhead
- Can switch models easily (Bedrock supports multiple providers)

### Model Configuration
- Model: Claude 3 Sonnet (balance of quality and cost)
- Temperature: 0.3 (low creativity, high consistency for scheduling)
- Max tokens: 1024 (responses should be concise)
- Stop sequences: None (let the model complete naturally)

---

## 4. Prompt Engineering

### System Prompt Design Philosophy
[Document how the system prompt shapes AI behavior. What persona does it have? What are the rules? What format does it output?]

### Prompt Iteration Methodology
1. **Version 1:** Write initial prompt based on product requirements
2. **Test:** Run 20+ test cases covering common and edge scenarios
3. **Evaluate:** Score each response on: relevance (1-5), accuracy (1-5), action correctness (pass/fail)
4. **Iterate:** Identify failure patterns, adjust prompt
5. **Repeat:** Until >90% of test cases pass
6. **Document:** Version history with test results

### See also: `docs/product/ai_prompts.md`

---

## 5. Inference

### Request Flow
[Detail the end-to-end flow from user input to AI response]

1. User taps mic and speaks (or types)
2. **Free tier:** Apple Speech transcribes on-device -> text sent to API
3. **Premium tier:** Audio uploaded to S3 -> AWS Transcribe converts to text
4. Backend receives text message via POST /ai/chat
5. Context Builder assembles prompt (system prompt + user data + conversation history + current message)
6. Bedrock invoked with assembled prompt
7. Response parsed: extract natural language text + action JSON
8. If action present: validate action, store as "pending confirmation"
9. Return response to iOS: text + action card + audio URL (if premium)
10. User confirms/rejects action -> if confirmed, execute (create event, task, etc.)

### Latency Budget
| Step | Target | Actual (measure) |
|------|--------|-------------------|
| Speech-to-text (Apple) | <1s | [Measure] |
| API round trip | <100ms | [Measure] |
| Context building | <200ms | [Measure] |
| Bedrock inference | <3s | [Measure] |
| Action execution | <500ms | [Measure] |
| Polly TTS (premium) | <1s | [Measure] |
| **Total (free)** | **<4s** | [Measure] |
| **Total (premium)** | **<5s** | [Measure] |

---

## 6. Evaluation

### How do we measure AI quality?

| Metric | Definition | Target | How Measured |
|--------|-----------|--------|-------------|
| Action Accuracy | % of AI-proposed actions that users confirm | >75% | confirmed / (confirmed + rejected) |
| Response Relevance | User doesn't need to rephrase/retry | >85% | 1 - (retry rate) |
| Gatekeeper Fairness | Legitimate reasons approved, non-legitimate denied | >90% agreement with human evaluation | Manual review of sample |
| Hallucination Rate | AI references events/tasks that don't exist | <2% | Automated validation of action params |
| Latency SLA | End-to-end response time | <5s p95 | CloudWatch metrics |
| Cost per Query | Average Bedrock cost per user interaction | <$0.05 | Token usage * pricing |

### Evaluation Process
- **Weekly:** Sample 50 random conversations, manually score for quality
- **Monthly:** Full evaluation across all metrics, identify trends
- **Per-release:** A/B test prompt changes against baseline

---

## 7. Feedback Loop

### How user feedback improves the AI

[Describe how confirmed/rejected actions, user corrections, and explicit feedback flow back to improve the system]

1. **Implicit feedback:** When users confirm an AI action, it validates the AI's understanding. When they reject, it signals a failure. Track confirm/reject ratios by action type.
2. **Explicit feedback:** Users can flag bad AI responses. Flagged responses are queued for manual review.
3. **Behavioral patterns:** If a user consistently reschedules AI-created events to different times, the AI should learn their preference (e.g., "this user prefers morning gym, not evening")
4. **Prompt refinement cycle:** Aggregate feedback weekly, identify failure patterns, update system prompt, test, deploy

### Current Limitation (MVP)
We don't fine-tune the model. Improvements come through prompt engineering, not model training. Post-MVP, we may explore:
- Few-shot examples from high-quality interactions
- User-specific preference learning (stored as structured data, injected into context)
- RAG (Retrieval Augmented Generation) for user-specific context

---

## 8. Monitoring

### Production Monitoring Dashboard

| Metric | Source | Alert Threshold |
|--------|--------|----------------|
| Bedrock invocation errors | CloudWatch | >5% error rate |
| Bedrock latency p95 | CloudWatch | >5s |
| Token usage per day | Bedrock logs | >$50/day (cost alert) |
| AI query volume | API Gateway logs | Anomaly detection |
| Action confirmation rate (daily) | Application logs | <60% (quality degradation) |
| Free tier query exhaustion rate | DynamoDB | >50% of free users hitting limit |
| Transcribe errors | CloudWatch | >3% error rate |

### Incident Response
- If AI quality degrades: rollback to previous prompt version
- If costs spike: enable token budgeting, reduce context window size
- If latency spikes: switch to smaller model (Claude 3 Haiku)
