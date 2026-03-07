# BetterSelf -- Developer Roadmaps & Sync Plan

## Team Overview

| | Dev A | Dev B |
|---|-------|-------|
| **Background** | CS background, Python, data science | Strong backend/AWS, Flutter experience |
| **Primary Track** | Product + AI Features + iOS UI | AWS Infrastructure + Backend API + AI Integration |
| **Learning Goals** | PM skills, AI/ML lifecycle, basic AWS | iOS/Swift, AI/ML integration, prompt engineering |
| **Career Goal** | PM role (AI-powered products) | Full-stack + AI/ML engineering |
| **Git Branch** | `feature/dev-a-*` | `feature/dev-b-*` |

## Key Principle: Cross-Exposure

Both developers get hands-on experience across ALL layers of the stack:

- **Dev A** does iOS UI + AI prompt engineering + PM artifacts + basic AWS tasks (S3, DynamoDB CRUD, CloudWatch monitoring)
- **Dev B** does AWS infra + backend APIs + AI/ML integration (Bedrock, Transcribe, Polly) + iOS features (widgets, Siri, Live Activities)
- **AWS complexity guide for Dev A:**
  - Suitable: S3 (file storage), DynamoDB (read/write items), CloudWatch (view logs/metrics), Cognito (understand auth flow), Pinpoint (analytics config)
  - Too complex for now: VPC/networking, security groups, CDK, IAM policies, Lambda deployment config -- Dev B owns these

---

## Phase 0: Pre-Interview Sprint (March 6-17)

**Dev A has a PM interview at IBM on March 17.** The IBM role focuses on AI-powered products, AI/ML lifecycle understanding, product strategy, Agile practices, responsible AI, and data-driven decision making.

**This 11-day sprint front-loads work that directly maps to the IBM PM job description.** Dev A produces real PM artifacts and gets hands-on AI/ML experience they can discuss in the interview.

### Dev A -- Pre-Interview Sprint (March 6-17)

The goal: produce tangible artifacts and hands-on experience Dev A can speak to in the interview. Each task maps to a specific IBM PM job requirement.

#### Days 1-3: Product Strategy & AI/ML Lifecycle

| Task | IBM PM Skill Mapped | Deliverable |
|------|---------------------|-------------|
| Write PRD for AI Secretary feature | "Define product strategy aligned with user needs and business goals" | `docs/product/ai_secretary_prd.md` |
| Document the AI/ML data lifecycle | "Understanding of AI, ML, or data lifecycle concepts" | `docs/product/ai_ml_lifecycle.md` |
| Create user personas and journey maps | "Advocate for user experience" | Section in PRD |

**PRD should include:** Problem statement, target personas, user stories (as a [role] I want [goal] so that [benefit]), success metrics, prioritized feature list with MoSCoW framework, technical constraints, competitive landscape (Opal, one sec, Fantastical, Motion).

**AI/ML Lifecycle doc should cover:**
1. **Data Collection** -- What data feeds the AI? (Calendar events, tasks, habits, blocking history, user preferences, conversation history)
2. **Data Pipeline** -- How does data flow from user actions to the LLM context window?
3. **Model Selection** -- Why Bedrock/Claude? Trade-offs vs GPT-4, Gemini, open-source models
4. **Prompt Engineering** -- How system prompts shape AI behavior; iteration methodology
5. **Inference** -- Request flow: user input -> context building -> LLM call -> action parsing
6. **Evaluation** -- How to measure AI quality (response relevance, action accuracy, user satisfaction)
7. **Feedback Loop** -- How user confirmations/rejections improve future responses
8. **Monitoring** -- Token usage, latency, error rates, cost per query

#### Days 3-5: Responsible AI & Sprint Planning

| Task | IBM PM Skill Mapped | Deliverable |
|------|---------------------|-------------|
| Create Responsible AI Framework | "Incorporate responsible AI principles such as transparency, fairness, and compliance" | `docs/product/responsible_ai.md` |
| Write Sprint Plan for Phase A | "Agile practices such as sprint planning and iterative delivery" | `docs/product/sprint_plans.md` |
| Define product KPIs and analytics plan | "Analyze data, use product analytics tools, and interpret metrics" | `docs/product/analytics_plan.md` |

**Responsible AI Framework should cover:**
- **Transparency:** What does the AI do with user data? How do we communicate AI limitations? What happens when the AI makes a mistake? How does the user know when AI created an event vs a human?
- **Fairness:** Does the AI gatekeeper treat all reasons equally? Are there biases in how it evaluates override requests? How do we prevent the AI from being too strict or too lenient?
- **Privacy & Compliance:** Data minimization, user consent flows, GDPR data export/deletion, what data is sent to Bedrock vs stays on-device, retention policies (90-day TTL on conversations)
- **Accountability:** Logging AI decisions for auditability, user ability to report bad AI behavior, human override always available (even in strict mode, with cooldown)

**Sprint Plans should include:**
- 2-week sprint breakdown for Phase A (4 sprints)
- User stories with acceptance criteria and story points
- Sprint goals and success criteria
- Velocity tracking plan
- Backlog prioritization using RICE or MoSCoW framework

**Analytics Plan should include:**
- Key metrics: DAU/MAU, focus session completion rate, AI query volume, avg session duration, premium conversion rate
- Per-feature metrics: AI action accuracy (confirmed vs rejected), gatekeeper override rate, calendar events created by AI, habit streak retention
- Tool: AWS Pinpoint for event tracking, CloudWatch dashboards for backend metrics
- Review cadence: weekly metrics review, monthly product review

#### Days 5-8: Hands-On AI/ML Work

| Task | IBM PM Skill Mapped | Deliverable |
|------|---------------------|-------------|
| Write and iterate AI secretary system prompt | "Translate technical concepts into clear product requirements" | `docs/product/ai_prompts.md` + tested prompts |
| Write AI gatekeeper prompt and test scenarios | "Translate technical concepts" + Responsible AI | Test results documented |
| Basic AWS hands-on: S3, DynamoDB, CloudWatch | "Understanding of AI, ML, or data lifecycle concepts" (infra context) | Hands-on experience to discuss |

**AI Prompt Engineering:**
- Write the system prompt for the AI secretary (define persona, capabilities, response format, action JSON structure)
- Write the gatekeeper prompt (what's legitimate, what's not, tone, firmness level)
- Test both prompts using the AWS Bedrock console or a Python script calling Bedrock API
- Document 20+ test cases with inputs and expected outputs
- Iterate on prompts based on test results (this IS the ML lifecycle in action)
- Document the iteration process (version 1 -> test -> issues found -> version 2 -> test -> improved)

**Basic AWS Hands-On (Dev B helps set up, Dev A operates):**
- Upload a file to S3, generate a presigned URL, download it
- Write an item to DynamoDB, read it back, update it, delete it (basic CRUD)
- Look at CloudWatch logs from Lambda, understand log groups and metrics
- Navigate the Cognito console, understand user pools and tokens conceptually

#### Days 8-11: Synthesis & Interview Prep

| Task | IBM PM Skill Mapped | Deliverable |
|------|---------------------|-------------|
| Create a product pitch deck (5-7 slides) | "Communicate product vision and progress to stakeholders" | Slide deck or doc |
| Practice articulating the AI/ML lifecycle | "Clear communication and storytelling skills" | Talking points |
| Start iOS project setup (M1) | Technical credibility | Xcode project building |

**Product Pitch Deck:**
- Slide 1: Problem (people lose hours to phone addiction + manual schedule management)
- Slide 2: Solution (BetterSelf -- AI-powered blocking + voice-first calendar secretary)
- Slide 3: AI/ML Architecture (data lifecycle diagram, model choice rationale)
- Slide 4: Responsible AI approach (transparency, fairness, compliance)
- Slide 5: KPIs and success metrics (how we measure product-market fit)
- Slide 6: Roadmap and sprint plan (Agile delivery approach)
- Slide 7: Competitive advantage (AI gatekeeper concept, voice-first interaction)

### Dev B -- Pre-Interview Sprint (March 6-17)

While Dev A focuses on PM artifacts, Dev B starts building the foundation.

| Days | Task | Details |
|------|------|---------|
| 1-3 | M9: CDK Foundation | VPC, subnets, security groups, base stacks |
| 3-5 | M10: Auth Infra | Cognito user pool, identity providers |
| 5-7 | M11: Database Setup | DynamoDB tables, Aurora cluster |
| 7-9 | M12: Lambda + API Gateway | FastAPI project, Mangum, health check |
| 9-11 | Help Dev A with AWS hands-on | Set up S3 bucket and DynamoDB table for Dev A to practice with. Pair on prompt testing via Bedrock console. |

**Sync during this phase:** Daily 15-min standup. Dev B reviews Dev A's PM documents for technical accuracy. Dev A reviews Dev B's CDK code to learn AWS concepts.

---

## Phase 1: iOS App Foundation (Weeks 3-6)

After the interview, both devs shift to building the product.

### Dev A -- Weeks 3-6

| Week | Milestone | Task | PM Angle |
|------|-----------|------|----------|
| 3 | M1-M2 | Project setup + data models (pair with Dev B) | Define acceptance criteria for each model |
| 3-4 | M3 | Tab navigation + home dashboard | Write user stories first, then build |
| 4-5 | M4 | Focus mode UI (profiles, timer, editor) | Document UX decisions and trade-offs |
| 5-6 | M8 | AI chat UI + Apple Speech integration | Own the AI interaction design end-to-end |
| 5-6 | -- | Basic AWS: Monitor CloudWatch logs from Dev B's APIs | Practice reading metrics, identify issues |

**PM Deliverables each sprint:** Dev A writes a 1-page sprint retrospective: what shipped, what was learned, what to improve. This builds the "iterative delivery" muscle.

### Dev B -- Weeks 3-6

| Week | Milestone | Task | AI Angle |
|------|-----------|------|----------|
| 3 | M1-M2 | Project setup + data models (pair with Dev A) | -- |
| 3-4 | M13 | AI + Voice services (Bedrock, Transcribe, Polly) | Design the AI secretary system prompt (pair with Dev A) |
| 4-5 | M14-M15 | User API + Blocking API | -- |
| 5-6 | M16 | Calendar API | Build AI-powered schedule optimization endpoint |
| 5-6 | M5 | FamilyControls integration (iOS) | Cross-exposure: learn FamilyControls framework |

**AI Focus:** Dev B owns the Bedrock integration end-to-end. Uses Dev A's prompt documents as the spec. Tests prompts programmatically and shares results with Dev A for product-level evaluation.

### Sync Point 1 -- End of Week 4

**Deliverables:**
- Dev A: Dashboard + Focus UI built, user stories documented, sprint retro written
- Dev B: Auth + Database + Lambda deployed, User/Blocking APIs working

**Discuss:** API contract review, demo progress, Dev A's first CloudWatch walkthrough

---

## Phase 2: Core Features (Weeks 6-8)

### Dev A -- Weeks 6-8

| Week | Milestone | Task | PM/AI Angle |
|------|-----------|------|-------------|
| 6-7 | M6 | Calendar UI (month/week/day views) | Define calendar UX requirements doc |
| 7 | M7 | Calendar integration (EventKit + Google) | Learn REST API integration, OAuth concepts |
| 7-8 | M8 | AI chat (continued) -- action confirmations, conversation history | Own the AI conversation UX, test prompt quality |
| 7-8 | -- | Basic AWS: Write blocking session data to DynamoDB via a simple Python script | Hands-on data pipeline experience |

### Dev B -- Weeks 6-8

| Week | Milestone | Task | AI Angle |
|------|-----------|------|----------|
| 6-7 | M17 | AI Secretary API (core AI endpoint) | Build context builder, action parser, Bedrock orchestration |
| 7 | M18 | Voice Processing API (Transcribe -> Bedrock -> Polly) | End-to-end voice AI pipeline |
| 7-8 | M19 | Tasks + Habits API | Build AI-powered task prioritization |
| 8 | M20 | Push Notifications (SNS + EventBridge) | Daily briefing AI generation |

### Sync Point 2 -- End of Week 7

**Deliverables:**
- Dev A: All iOS UI screens built, calendar integration working
- Dev B: All backend APIs deployed, AI secretary responding to prompts

**Discuss:** First end-to-end test (Dev A's app hits Dev B's APIs), AI prompt quality review together, scope check

---

## Phase 3: Integration (Weeks 8-10)

Both devs work more closely together in this phase.

### Dev A -- Weeks 8-10

| Week | Milestone | Task | PM/AI/AWS Angle |
|------|-----------|------|-----------------|
| 8 | M21 | Auth integration (Cognito SDK in Swift) | Understand auth architecture by implementing it |
| 8-9 | M22 | API client + offline sync engine | Learn about data synchronization patterns |
| 9 | M23 | AI integration (connect chat to Bedrock via backend) | Test AI quality in production context, log issues |
| 9-10 | M29 | Onboarding flow | Own the onboarding UX -- this is product strategy work |
| 10 | -- | AWS: Set up Pinpoint analytics events from iOS | Track the KPIs defined in analytics plan |

### Dev B -- Weeks 8-10

| Week | Milestone | Task | iOS/AI Angle |
|------|-----------|------|--------------|
| 8-9 | M24-M25 | Blocking sync + Calendar sync (help Dev A) | Pair on complex sync logic |
| 9 | M26 | iOS Widgets (WidgetKit) | Learn SwiftUI in an isolated context |
| 9-10 | M27 | Live Activities (lock screen timer) | ActivityKit -- another good iOS learning task |
| 10 | M28 | Siri Shortcuts (App Intents) | AI-adjacent: voice command -> action mapping |

### Sync Point 3 -- End of Week 9

**Deliverables:**
- Full app connected to backend, all features work end-to-end
- Dev A has Pinpoint analytics sending events

**Discuss:** Full device walkthrough, offline testing, AI gatekeeper testing, analytics data review

---

## Phase 4: Polish & Launch (Weeks 10-12)

### Dev A -- Weeks 10-12

| Week | Milestone | Task | PM Angle |
|------|-----------|------|----------|
| 10 | M30 | Polish + accessibility | Own accessibility requirements (VoiceOver, Dynamic Type) |
| 10-11 | M31 | Testing (iOS) -- XCTest, XCUITest | Write test cases from user stories |
| 11 | -- | Product: Write App Store listing copy | Product marketing -- storytelling |
| 11-12 | M32 | App Store submission | Manage the launch checklist |
| 12 | -- | Product: Post-launch metrics review plan | Define what success looks like week 1, month 1 |

### Dev B -- Weeks 10-12

| Week | Milestone | Task |
|------|-----------|------|
| 10 | M31 | Testing (backend) -- pytest, integration tests |
| 10-11 | -- | CloudWatch dashboards, alarms, Bedrock cost monitoring |
| 11 | -- | Security review: IAM roles, rate limiting, encryption audit |
| 11-12 | M32 | Production deploy, SSL, domain, scaling config |

### Sync Point 4 -- End of Week 11

Feature freeze. TestFlight beta. Final testing. Submit to App Store.

---

## Dev A -- PM Artifacts Summary

All PM deliverables Dev A produces during the project (great for portfolio and interview talking points):

| Document | IBM PM Skill | When |
|----------|-------------|------|
| `docs/product/ai_secretary_prd.md` | Product strategy, user needs, backlog management | Pre-interview (Days 1-3) |
| `docs/product/ai_ml_lifecycle.md` | AI/ML data lifecycle understanding | Pre-interview (Days 1-3) |
| `docs/product/responsible_ai.md` | Responsible AI principles (transparency, fairness, compliance) | Pre-interview (Days 3-5) |
| `docs/product/sprint_plans.md` | Agile sprint planning, story points, velocity | Pre-interview (Days 3-5) |
| `docs/product/analytics_plan.md` | Product analytics, KPIs, data-driven decisions | Pre-interview (Days 3-5) |
| `docs/product/ai_prompts.md` | Translating ML concepts into product requirements | Pre-interview (Days 5-8) |
| Product pitch deck | Stakeholder communication, storytelling | Pre-interview (Days 8-11) |
| Sprint retrospectives (x6) | Iterative delivery, continuous improvement | Every 2 weeks during build |
| App Store listing copy | Product marketing and positioning | Week 11 |
| Post-launch metrics plan | Analytics interpretation, product outcomes | Week 12 |

---

## Dev B -- AI/ML Exposure Summary

AI/ML work Dev B owns or co-owns during the project:

| Task | AI/ML Skill | When |
|------|------------|------|
| Bedrock model setup + invocation code | LLM API integration | Weeks 3-4 (M13) |
| AI secretary system prompt design | Prompt engineering | Weeks 3-4 (pair with Dev A) |
| AI gatekeeper prompt + evaluation logic | Responsible AI implementation | Weeks 4-5 (pair with Dev A) |
| Context builder (schedule + tasks + history -> prompt) | Data pipeline for AI | Weeks 6-7 (M17) |
| Action parser (LLM response -> structured JSON -> execution) | AI output structuring | Weeks 6-7 (M17) |
| Voice pipeline (Transcribe -> Bedrock -> Polly) | Multi-modal AI pipeline | Week 7 (M18) |
| AI-powered task prioritization | ML-informed features | Week 7-8 (M19) |
| Daily briefing generation | AI content generation | Week 8 (M20) |
| Schedule optimization via Bedrock | AI-powered decision making | Week 6-7 (M16) |
| Siri -> AI command mapping | Voice AI integration | Week 10 (M28) |

---

## AWS Exposure for Dev A

Entry-level AWS tasks throughout the project (with Dev B's guidance):

| Task | AWS Service | Complexity | When |
|------|------------|------------|------|
| Upload/download files, generate presigned URL | S3 | Beginner | Pre-interview (Days 5-8) |
| Write/read/update items in a table | DynamoDB | Beginner | Pre-interview (Days 5-8) |
| View Lambda logs, understand log groups | CloudWatch | Beginner | Weeks 5-6 |
| Understand user pools, tokens, auth flow | Cognito | Conceptual | Weeks 3-4 |
| Configure event tracking from iOS | Pinpoint | Beginner | Weeks 9-10 |
| View API Gateway request logs | CloudWatch | Beginner | Weeks 8-9 |
| Navigate the AWS Console, understand regions/services | General | Beginner | Throughout |

**Not for Dev A (too complex):** VPC configuration, security groups, CDK/IaC, IAM policies, Lambda deployment, NAT gateways, Aurora cluster management

---

## Collaboration Approach

- **Branching:** Feature branches off `develop`, merged via pull requests
- **Code Reviews:** Every PR requires review from the other developer
- **Sync Points:** 4 scheduled checkpoints (reduced from 6 to match compressed timeline)
- **API Contract First:** Both agree on endpoint shapes before building (see `docs/design/api_contract.md`)
- **Daily:** 15-min async standup (what I did, what I'm doing, blockers)
- **Weekly:** 30-min video call to demo, review, and plan
- **PR Reviews:** Review within 24 hours. Dev B gives iOS architecture feedback to Dev A. Dev A gives product/UX feedback to Dev B.

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Dev A's interview prep takes away from project time | Pre-interview artifacts ARE project deliverables (PRD, lifecycle doc, prompts). No wasted effort. |
| API contract mismatch | Create `docs/design/api_contract.md` at SP1, both sign off on changes. |
| Dev A blocked on complex iOS | Dev B pairs on hard tasks (FamilyControls, calendar sync). |
| Dev B's iOS learning curve | Start with isolated WidgetKit/Siri tasks. Dev A reviews PRs. |
| Cross-exposure slows velocity | Limit cross-tasks to 20% of each sprint. Core track is primary. |
| Falling behind schedule | Each sync point includes scope check. Cut: meeting prep, advanced analytics, Apple Watch. Keep: blocking, AI chat, calendar. |
| FamilyControls entitlement delayed | Apply in Week 1. Build nudge UI as fallback. |

---

## Definition of Done (per milestone)

1. All planned features work as described in the milestone file
2. Code is merged to `develop` via reviewed PR
3. No known crashes or critical bugs
4. Milestone file status updated to "Completed" with "What Was Built" section
5. Any deviations from the plan documented in the milestone's "Notes" section
6. **Dev A additionally:** Sprint retro written, user stories documented
