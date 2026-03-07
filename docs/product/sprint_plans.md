# BetterSelf -- Sprint Plans

> **Author:** Dev A
> **Status:** Draft
> **Methodology:** Agile Scrum, 2-week sprints
> **Sprint cadence:** Planning on Monday, Retro on Friday of week 2

---

## Sprint 0: Pre-Interview Sprint (March 6-17)

**Goal:** Produce PM artifacts and gain hands-on AI/ML experience

### Dev A Sprint Backlog
| Story | Points | Priority | Status |
|-------|--------|----------|--------|
| Write AI Secretary PRD (personas, user stories, metrics) | 5 | Must | To Do |
| Document AI/ML data lifecycle end-to-end | 5 | Must | To Do |
| Create responsible AI framework | 3 | Must | To Do |
| Define product KPIs and analytics plan | 3 | Must | To Do |
| Write and test AI secretary system prompt (10+ test cases) | 5 | Must | To Do |
| Write and test AI gatekeeper prompt (10+ test cases) | 3 | Must | To Do |
| AWS hands-on: S3 upload/download, DynamoDB CRUD | 2 | Should | To Do |
| Create product pitch deck (5-7 slides) | 3 | Should | To Do |
| Practice interview talking points | 2 | Must | To Do |

**Total:** 31 points | **Velocity estimate:** first sprint, establish baseline

### Dev B Sprint Backlog
| Story | Points | Priority | Status |
|-------|--------|----------|--------|
| M9: Deploy VPC, subnets, security groups via CDK | 5 | Must | To Do |
| M10: Configure Cognito user pool + identity providers | 5 | Must | To Do |
| M11: Deploy DynamoDB tables + Aurora cluster | 5 | Must | To Do |
| M12: Deploy FastAPI Lambda + API Gateway health check | 5 | Must | To Do |
| Set up S3 bucket and DynamoDB table for Dev A hands-on | 1 | Should | To Do |
| Review Dev A's PM docs for technical accuracy | 2 | Should | To Do |

**Total:** 23 points

### Sprint 0 Retro Template
- What went well?
- What didn't go well?
- What should we change?
- Velocity achieved: __ / __ points

---

## Sprint 1 (Weeks 3-4)

**Goal:** Xcode project setup, core iOS UI screens, AI services configured

### Dev A
| Story | Points | Priority | Acceptance Criteria |
|-------|--------|----------|---------------------|
| M1: Create Xcode project with design system | 3 | Must | Project builds, colors/typography render in preview |
| M2: Define SwiftData models + mock data | 3 | Must | All 8 models defined, MockDataService returns sample data |
| M3: 3-tab navigation + home dashboard | 5 | Must | Tabs switch, dashboard shows greeting + summary cards |
| M4: Focus mode UI (profile list + timer) | 5 | Must | Can create profile, start timer, see countdown |
| Write sprint retro | 1 | Must | Retro document completed |

### Dev B
| Story | Points | Priority | Acceptance Criteria |
|-------|--------|----------|---------------------|
| M13: Bedrock integration + system prompt | 5 | Must | Can invoke Bedrock, get structured response |
| M13: Transcribe + Polly setup | 3 | Must | Can transcribe audio, generate speech |
| M14: User registration + profile API | 3 | Must | POST /auth/register and GET /users/me work |
| M15: Blocking profiles CRUD API | 3 | Must | Full CRUD + session logging works |
| M5: FamilyControls integration (iOS) | 5 | Should | Authorization flow works on device |

---

## Sprint 2 (Weeks 5-6)

**Goal:** Calendar + AI chat UI, core backend APIs

[Dev A fills in based on milestones M6, M8 + CloudWatch monitoring task]

[Dev B fills in based on milestones M16, M17]

---

## Sprint 3 (Weeks 7-8)

**Goal:** Calendar integration, AI Secretary API, voice pipeline

[Plan during Sprint 2 retro based on velocity]

---

## Sprint 4 (Weeks 9-10)

**Goal:** Full integration, widgets, onboarding

[Plan during Sprint 3 retro]

---

## Sprint 5 (Weeks 11-12)

**Goal:** Polish, testing, launch

[Plan during Sprint 4 retro]

---

## Velocity Tracking

| Sprint | Dev A Planned | Dev A Actual | Dev B Planned | Dev B Actual |
|--------|--------------|-------------|--------------|-------------|
| Sprint 0 | 31 | | 23 | |
| Sprint 1 | 17 | | 19 | |
| Sprint 2 | | | | |
| Sprint 3 | | | | |
| Sprint 4 | | | | |
| Sprint 5 | | | | |

---

## Backlog Prioritization Framework: RICE

We use RICE scoring to prioritize features:

- **Reach:** How many users does this impact per month?
- **Impact:** How much does this move the needle? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- **Confidence:** How sure are we about the estimates? (100%=high, 80%=medium, 50%=low)
- **Effort:** Person-days to build

**RICE Score = (Reach x Impact x Confidence) / Effort**

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|-----------|--------|-----------|----------|
| AI chat (voice scheduling) | 1000 | 3 | 80% | 10 | 240 | 1 |
| App blocking (FamilyControls) | 1000 | 3 | 50% | 12 | 125 | 2 |
| Daily briefing | 800 | 2 | 80% | 5 | 256 | 1 |
| Calendar sync | 700 | 2 | 80% | 8 | 140 | 2 |
| [Add more features] | | | | | | |
