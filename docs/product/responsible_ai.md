# BetterSelf -- Responsible AI Framework

> **Author:** Dev A
> **Status:** Draft
> **Purpose:** Define principles and practices for responsible, ethical AI in BetterSelf. Covers transparency, fairness, privacy, and accountability.

---

## 1. Transparency

### 1.1 AI Disclosure
[How do we make it clear to users when AI is acting vs when they are in control?]

- AI-created calendar events are visually distinct (purple color, "AI" badge)
- AI responses clearly come from the "assistant" with a bot avatar (never impersonate a human)
- When the AI takes an action, it always explains what it did and why
- Action confirmations show exactly what will change before the user approves

### 1.2 Limitations Communication
[How do we communicate what the AI can and cannot do?]

- Onboarding includes a "What your AI assistant can do" screen with clear scope
- AI responds "I can't do that yet" for out-of-scope requests (not hallucinate an answer)
- Help/FAQ section documents AI capabilities and known limitations

### 1.3 Data Usage Transparency
[How do we tell users what data the AI uses?]

- [Define: what data is sent to Bedrock? What stays on device? How long is data retained?]
- [Define: privacy policy language for AI features]
- [Define: in-app data usage explanation screen]

---

## 2. Fairness

### 2.1 AI Gatekeeper Fairness
[The AI gatekeeper evaluates whether a user's reason for overriding a focus session is "legitimate." This is a sensitive area -- how do we ensure fairness?]

- [Define: what makes a reason "legitimate" vs "not legitimate"?]
- [Define: are there cultural or contextual biases in this evaluation?]
- [Define: how do we prevent the AI from being unfairly strict with certain types of reasons?]
- [Define: is the evaluation consistent across users?]
- [Define: what audit process ensures fairness over time?]

### 2.2 Schedule Optimization Fairness
[When the AI optimizes schedules, does it have biases?]

- [Define: does it prioritize work over personal life? How do we ensure work-life balance?]
- [Define: does it handle different work patterns fairly (night owls vs early birds)?]

### 2.3 Inclusive Design
- AI uses gender-neutral language
- Voice options should include diverse voices (future: multiple Polly voices)
- Calendar handles diverse holidays and cultural events

---

## 3. Privacy & Compliance

### 3.1 Data Minimization
[What is the minimum data needed for each AI feature to work?]

| Feature | Data Needed | Data NOT Needed |
|---------|------------|-----------------|
| Schedule events | Calendar events, user message | App usage data, location |
| Daily briefing | Events, tasks, habits | Conversation history |
| AI gatekeeper | User's stated reason | Their actual app usage |
| [Add more] | | |

### 3.2 User Consent
[How do we get and manage consent?]

- [Define: what permissions do we request and when?]
- [Define: can users use the app without AI features?]
- [Define: can users opt out of specific data collection?]

### 3.3 GDPR / Privacy Compliance
- Data export: users can download all their data (API endpoint: GET /users/me/export)
- Data deletion: users can delete their account and all data (API endpoint: DELETE /users/me)
- Data retention: conversation history auto-deleted after 90 days
- Voice audio: transcribed and deleted within 24 hours, never stored long-term
- Third-party data sharing: NO user data is shared with or sold to third parties
- Bedrock data handling: AWS Bedrock does not use customer inputs to train models

### 3.4 Children's Privacy
- BetterSelf is designed for self-management (13+ audience), NOT parental controls
- No collection of data from children under 13
- FamilyControls used for individual mode, not family mode

---

## 4. Accountability

### 4.1 AI Decision Logging
[How do we audit AI decisions?]

- All AI interactions logged in DynamoDB (user message, AI response, action proposed, user decision)
- Gatekeeper decisions logged: reason provided, AI evaluation, outcome (approved/denied)
- Logs retained for 90 days for audit purposes

### 4.2 Human Override
[Users always maintain ultimate control]

- Even in "strict mode," there is always an emergency override (with cooldown)
- Users can disable AI features entirely and use the app manually
- Users can delete AI conversation history at any time

### 4.3 Error Handling
[What happens when the AI makes a mistake?]

- [Define: how do users report bad AI behavior?]
- [Define: what is the escalation process?]
- [Define: how quickly do we respond to AI quality issues?]

### 4.4 Regular Audits
- Weekly: sample 50 AI conversations, score for quality and fairness
- Monthly: review gatekeeper decisions for bias patterns
- Quarterly: comprehensive responsible AI review with updated metrics

---

## 5. Implementation Checklist

- [ ] AI-created events visually tagged with "AI" badge
- [ ] Action confirmation required before any AI-initiated change
- [ ] Privacy policy covers AI data usage
- [ ] Data export and deletion endpoints implemented
- [ ] Conversation TTL (90 days) configured in DynamoDB
- [ ] Voice audio auto-deletion (24 hours) configured in S3
- [ ] Gatekeeper decision logging implemented
- [ ] AI capability documentation in onboarding
- [ ] "I can't do that" fallback responses for out-of-scope requests
- [ ] Emergency override available in strict mode
- [ ] Gender-neutral AI language in system prompt
- [ ] Weekly quality audit process established
