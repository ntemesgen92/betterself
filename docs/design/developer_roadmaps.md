# BetterSelf -- Developer Roadmaps & Sync Plan

## Team Overview

| | Dev A | Dev B |
|---|-------|-------|
| **Strengths** | AI interest, learning iOS | Backend/AWS strong, Flutter experience |
| **Primary Track** | iOS UI + AI Features | AWS Infrastructure + Backend API |
| **Learning Goals** | AI integration, iOS development | iOS/Swift, AI/ML integration |
| **Git Branch** | `feature/ios-*` | `feature/backend-*` |

## Collaboration Approach

- **Branching:** Feature branches off `develop`, merged via pull requests
- **Code Reviews:** Every PR requires review from the other developer
- **Sync Points:** 6 scheduled checkpoints where both developers sync, review progress, and agree on next steps
- **API Contract First:** Before building endpoints or clients, both agree on request/response shapes in a shared API spec
- **Shared Resources:** Both devs pair on Milestones 1-2 (project bootstrap) and Milestones 31-32 (testing + launch)

---

## Timeline Overview (12 Weeks)

```
Week:  1    2    3    4    5    6    7    8    9    10   11   12
       |    |    |    |    |    |    |    |    |    |    |    |
Dev A: [--Bootstrap--][---iOS UI---][--AI Chat--][Integration][Widgets+Polish][Test+Launch]
Dev B: [--Bootstrap--][--AWS Infra-][--Backend API----------][iOS Learn+Int][Test+Launch]
       |         |         |              |              |              |
      SP1       SP2       SP3            SP4            SP5           SP6
```

**SP = Sync Point**

---

## Sync Points

### Sync Point 1 -- Project Bootstrap (End of Week 1)

**When:** End of Week 1
**Duration:** 2-3 hours together
**Purpose:** Both developers start together to establish foundations

**Deliverables before sync:**
- [x] Xcode project created and building (pair together)
- [x] SwiftData models defined (pair together)
- [x] Mock data service working
- [x] Git repo configured with `main` and `develop` branches
- [x] CDK project initialized (Dev B starts)

**Discuss at sync:**
- Review data models -- do they cover all use cases?
- Agree on coding conventions (Swift style, Python style)
- Set up PR template and review expectations
- Dev B walks Dev A through the AWS architecture diagram
- Divide Week 2-3 milestones explicitly

---

### Sync Point 2 -- API Contract Agreement (End of Week 3)

**When:** End of Week 3
**Duration:** 3-4 hours together
**Purpose:** Agree on every API endpoint shape before building clients or servers

**Deliverables before sync:**
- Dev A: Tab navigation + home dashboard built (M3), focus mode UI started (M4)
- Dev B: CDK foundation deployed (M9), Cognito configured (M10), databases deployed (M11), Lambda + API Gateway health check working (M12)

**Discuss at sync:**
- Walk through and finalize the API contract document (see below)
- Agree on authentication flow (Cognito token format, header conventions)
- Agree on error response format
- Dev A demos the iOS UI progress
- Dev B demos the deployed infrastructure (health check, Cognito sign-up)
- Identify blockers or scope adjustments

**Key Artifact:** Create `docs/api_contract.md` with every endpoint, request/response shape, and status codes. Both developers sign off. Example:

```
POST /ai/chat
Authorization: Bearer <cognito-jwt>
Request:  { "message": "Schedule gym 3 times this week" }
Response: { "id": "...", "text": "I'll schedule...", "action": { "type": "create_event", ... }, "confirmed": false }
```

---

### Sync Point 3 -- Mock API + Core UI Checkpoint (End of Week 5)

**When:** End of Week 5
**Duration:** 2-3 hours together
**Purpose:** Dev B has core APIs deployed, Dev A has all major UI screens

**Deliverables before sync:**
- Dev A: Focus UI complete (M4), FamilyControls integrated (M5), calendar UI built (M6), AI chat UI with mock responses (M8 started)
- Dev B: User/Auth API (M14), Blocking API (M15), Calendar API started (M16), AI/Voice services configured (M13)

**Discuss at sync:**
- Dev A tests against Dev B's deployed staging APIs (first real connection test)
- Identify API contract mismatches and fix them
- Dev B reviews Dev A's iOS code -- suggest improvements
- Dev A walks Dev B through FamilyControls integration (complex area)
- Plan the AI prompt engineering together (shared interest)
- Discuss: is Aurora needed or can DynamoDB handle everything for MVP?

---

### Sync Point 4 -- Core Features Complete (End of Week 7)

**When:** End of Week 7
**Duration:** 3-4 hours together
**Purpose:** All core features built (separately), ready to integrate

**Deliverables before sync:**
- Dev A: Calendar integration working (M7), AI chat UI + Apple Speech complete (M8), all iOS screens functional with mock data
- Dev B: All backend APIs complete (M14-20), AI secretary responding to prompts via Bedrock, push notifications configured

**Discuss at sync:**
- End-to-end demo: Dev A runs app, Dev B monitors backend logs
- Test each API endpoint with real iOS requests
- Review AI secretary prompt -- test various commands together, refine
- Plan integration milestones (M21-25): who does what
- Dev B starts learning iOS by picking up a small feature (Siri Shortcuts M28 is a good starter)

**Key Artifact:** Record a list of all issues/bugs found during the end-to-end test

---

### Sync Point 5 -- Integration Complete (End of Week 9)

**When:** End of Week 9
**Duration:** 3-4 hours together
**Purpose:** App is fully connected to backend, all features work end-to-end

**Deliverables before sync:**
- Dev A: Auth integration (M21), API client + sync (M22), AI integration (M23), blocking sync (M24), calendar sync (M25)
- Dev B: Widgets (M26), Live Activities (M27), Siri Shortcuts (M28) -- Dev B's iOS learning milestones, with code review from Dev A

**Discuss at sync:**
- Full app walkthrough on a real device
- Test offline mode: airplane mode, queue operations, reconnect
- Test edge cases together: expired tokens, network errors, calendar conflicts
- Test AI gatekeeper flow with various override reasons
- Plan onboarding flow content and copy
- Decide: what needs polish vs what's good enough for MVP?
- Begin writing test cases for M31

---

### Sync Point 6 -- Feature Freeze + Launch Prep (End of Week 11)

**When:** End of Week 11
**Duration:** Full day together
**Purpose:** Feature freeze, testing, and App Store preparation

**Deliverables before sync:**
- Dev A: Onboarding flow (M29), polish + accessibility (M30)
- Dev B: Backend tests complete, monitoring dashboards set up
- Both: Unit tests + UI tests (M31)

**Discuss at sync:**
- Final full app test on multiple devices (iPhone SE, iPhone 16 Pro Max)
- Accessibility audit (VoiceOver, Dynamic Type)
- Review App Store listing copy
- Submit FamilyControls entitlement request (if not already done)
- Deploy to TestFlight, invite beta testers
- Create launch checklist
- Submit to App Store (M32)

---

## Dev A Roadmap -- iOS UI + AI Features

### Week 1: Bootstrap (with Dev B)

| Milestone | Task | Details |
|-----------|------|---------|
| M1 | Pair: Project Setup | Create Xcode project together, set up design system, add SPM dependencies |
| M2 | Pair: Data Models | Define SwiftData models together, create mock data service |

**Learning focus:** SwiftUI basics, Xcode navigation, Swift syntax

### Weeks 2-3: iOS UI Screens

| Milestone | Task | Details |
|-----------|------|---------|
| M3 | Tab Navigation + Dashboard | Build 3-tab layout, home dashboard with summary cards, settings shell |
| M4 | Focus Mode UI | Profile list, profile editor, timer screen, focus history |

**Learning focus:** SwiftUI layouts (VStack, HStack, ScrollView, NavigationStack), @Observable pattern

### Weeks 3-5: Core iOS Features

| Milestone | Task | Details |
|-----------|------|---------|
| M5 | FamilyControls | Integrate FamilyControls authorization, app picker, shield configuration (complex -- ask Dev B for help if stuck) |
| M6 | Calendar UI | Month/week/day views, event creation form |
| M8 | AI Chat UI + Voice | Push-to-talk interface, Apple Speech integration, voice waveform, conversation history, mock AI responses |

**Learning focus:** System frameworks (FamilyControls, EventKit, Speech), async/await, Combine

### Weeks 5-7: Calendar + AI Polish

| Milestone | Task | Details |
|-----------|------|---------|
| M7 | Calendar Integration | EventKit for Apple Calendar, Google Calendar REST API, sync engine |
| M8 | AI Chat (continued) | Refine voice UX, action confirmation cards, conversation persistence |
| -- | AI Prompts | Work with Dev B on AI secretary system prompt and gatekeeper prompt |

**Learning focus:** REST API integration, OAuth flows, AI prompt engineering

### Weeks 7-9: Integration

| Milestone | Task | Details |
|-----------|------|---------|
| M21 | Auth Integration | Connect Cognito SDK, sign-in/sign-up flows, token management |
| M22 | API Client + Sync | Build Swift API client, offline queue, background sync |
| M23 | AI Integration | Connect voice chat to backend AI, streaming responses, action confirmations |
| M24 | Blocking Sync | Sync blocking profiles/sessions with backend |
| M25 | Calendar Sync | Two-way calendar sync with conflict resolution |

**Learning focus:** Networking (URLSession/Alamofire), Cognito SDK, background tasks

### Weeks 9-11: Onboarding + Polish

| Milestone | Task | Details |
|-----------|------|---------|
| M29 | Onboarding Flow | Guided setup screens (goals, schedule, apps, calendar, AI intro) |
| M30 | Polish + Accessibility | Animations, haptics, VoiceOver, Dynamic Type, dark mode |
| M31 | Testing (iOS) | XCTest unit tests, XCUITest UI tests |

**Learning focus:** Accessibility APIs, animation, XCTest

### Weeks 11-12: Launch

| Milestone | Task | Details |
|-----------|------|---------|
| M31 | TestFlight | Distribute beta build, collect feedback |
| M32 | App Store Submission | Screenshots, listing, FamilyControls entitlement, submit for review |

---

## Dev B Roadmap -- Backend + AWS (then iOS)

### Week 1: Bootstrap (with Dev A)

| Milestone | Task | Details |
|-----------|------|---------|
| M1 | Pair: Project Setup | Help set up Xcode project, contribute to design system |
| M2 | Pair: Data Models | Define SwiftData models together, ensure alignment with backend schemas |
| M9 | AWS CDK Foundation | Initialize CDK project, deploy VPC, subnets, security groups |

**Learning focus:** Swift/SwiftUI basics (leverage Flutter knowledge), CDK project structure

### Weeks 2-3: AWS Infrastructure

| Milestone | Task | Details |
|-----------|------|---------|
| M10 | Auth Infrastructure | Cognito user pool, Apple + Google identity providers, API Gateway + authorizer |
| M11 | Database Setup | DynamoDB tables, Aurora Serverless v2 (if needed), CDK definitions |
| M12 | Lambda + API Gateway | FastAPI project, Mangum adapter, deploy pipeline, health check |

**Learning focus:** Cognito configuration, CDK patterns, FastAPI + Lambda

### Weeks 3-5: AI Services + First APIs

| Milestone | Task | Details |
|-----------|------|---------|
| M13 | AI + Voice Services | Bedrock integration, Transcribe + Polly setup, AI secretary system prompt |
| M14 | User + Auth API | Registration, profile CRUD, subscription endpoints |
| M15 | Blocking Rules API | Blocking profile CRUD, session logging, stats aggregation |

**Learning focus:** Bedrock API, prompt engineering, AI/ML integration

### Weeks 5-7: Core Backend APIs

| Milestone | Task | Details |
|-----------|------|---------|
| M16 | Calendar API | Event CRUD, sync endpoints, conflict detection, AI optimization |
| M17 | AI Secretary API | Chat endpoint, context building, action parsing, daily briefing generation |
| M18 | Voice Processing API | Audio upload -> Transcribe -> Bedrock -> Polly pipeline |
| M19 | Tasks + Habits API | Task CRUD, habit tracking, streak calculation |
| M20 | Push Notifications | SNS + APNs, daily briefing scheduler, focus reminders |

**Learning focus:** AI conversation design, voice pipeline optimization, EventBridge scheduling

### Weeks 7-9: iOS Learning + Support Integration

| Milestone | Task | Details |
|-----------|------|---------|
| M26 | iOS Widgets | WidgetKit implementation (good starter iOS task -- isolated, well-documented) |
| M27 | Live Activities | Focus timer on lock screen + Dynamic Island |
| M28 | Siri Shortcuts | App Intents for voice commands |
| -- | Support Dev A | Help debug integration issues, review PRs, pair on complex problems |

**Learning focus:** WidgetKit, ActivityKit, App Intents -- self-contained iOS features good for learning Swift

### Weeks 9-11: Testing + Monitoring

| Milestone | Task | Details |
|-----------|------|---------|
| M31 | Testing (Backend) | pytest unit tests, integration tests, load testing |
| -- | Monitoring | CloudWatch dashboards, alarms for errors/latency, Bedrock token usage tracking |
| -- | Security Review | Review IAM roles, API rate limiting, data encryption |

**Learning focus:** Testing patterns, observability, production readiness

### Weeks 11-12: Launch

| Milestone | Task | Details |
|-----------|------|---------|
| M31 | TestFlight Support | Monitor backend during beta testing, fix issues |
| M32 | Launch Prep | Production CDK deploy, SSL, domain setup, scaling configuration |

---

## Shared Milestones (Pair Together)

These milestones benefit from both developers working together:

| Milestone | Why Pair |
|-----------|----------|
| M1-M2 (Setup + Models) | Establish shared foundations, coding style, data model agreement |
| API Contract (SP2) | Both must agree on every endpoint shape |
| M17 (AI Secretary Prompt) | Both interested in AI -- design the prompt together |
| AI Gatekeeper Logic | Both interested in AI -- define what's "legitimate" together |
| M31-M32 (Test + Launch) | Both needed for comprehensive testing and launch prep |

---

## Risk Mitigation for Parallel Work

| Risk | Mitigation |
|------|-----------|
| API contract mismatch | Create `docs/api_contract.md` at SP2, update it as APIs evolve. Both devs sign off on changes. |
| Dev A blocked on complex iOS feature | Dev B available for pairing (has Flutter context). Schedule 30-min daily standups. |
| Dev B's iOS code quality (learning) | Dev A reviews all iOS PRs. Start with isolated features (widgets, Siri). |
| Merge conflicts | Keep clear ownership boundaries. Use feature branches. Sync develop branch at every SP. |
| One track falls behind | Each SP includes a scope check. Cut non-essential features (analytics, meeting prep) if behind. |
| FamilyControls entitlement delayed | Apply in Week 1. Build nudge/accountability mode as fallback (doesn't need entitlement). |

---

## Daily / Weekly Rituals

- **Daily:** 15-min async standup (Slack/Discord message: what I did, what I'm doing, blockers)
- **Weekly:** 30-min video call to review progress, demo features, discuss upcoming work
- **Sync Points:** Longer in-person or video sessions (2-4 hours) as described above
- **PR Reviews:** Review within 24 hours. Use comments for learning, not just approval.

---

## Definition of Done (per milestone)

A milestone is "done" when:
1. All planned features work as described in the milestone file
2. Code is merged to `develop` via reviewed PR
3. No known crashes or critical bugs
4. Milestone file status updated to "Completed" with "What Was Built" section
5. Any deviations from the plan documented in the milestone's "Notes" section
