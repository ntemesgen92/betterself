# BetterSelf

iOS productivity app combining intelligent app blocking with a voice-first AI calendar secretary.

## Core Features

- **Intelligent App Blocking** -- Uses Apple FamilyControls to block distracting apps, with an AI accountability gatekeeper that manages overrides
- **Voice-First AI Secretary** -- Professional AI assistant for calendar management, task prioritization, habit tracking, and daily briefings

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Swift + SwiftUI (iOS 17+) |
| Backend | Python (FastAPI) on AWS Lambda |
| Auth | AWS Cognito (email + Apple + Google sign-in) |
| Database | DynamoDB + Aurora Serverless v2 (PostgreSQL) |
| AI | AWS Bedrock (Claude) |
| Voice | Apple Speech (free) / AWS Transcribe + Polly (premium) |
| Infrastructure | AWS CDK (Python) |

## Project Structure

```
betterself/
├── docs/design/                    # Design documentation
│   ├── betterself_app_plan.md      # Master design document
│   ├── milestones/                 # 32 milestone plan files
│   │   ├── milestone_1_setup.plan.md
│   │   ├── ...
│   │   └── milestone_32_app_store.plan.md
│   └── diagrams/                   # Architecture diagrams (Python)
├── BetterSelf/                     # iOS app (Swift, coming soon)
└── backend/                        # Backend API + CDK (coming soon)
```

## Getting Started

See [docs/design/betterself_app_plan.md](docs/design/betterself_app_plan.md) for the full design document.

## Development Phases

1. **Phase A (Weeks 1-4):** iOS App Foundation -- UI, FamilyControls, Calendar, AI Chat
2. **Phase B (Weeks 4-6):** AWS Infrastructure -- CDK, Cognito, Databases, Lambda
3. **Phase C (Weeks 6-8):** Backend API -- User, Blocking, Calendar, AI, Voice, Tasks APIs
4. **Phase D (Weeks 8-10):** Integration -- Connect iOS app to backend
5. **Phase E (Weeks 10-12):** Widgets, Polish & Launch -- Widgets, Live Activities, Siri, Onboarding, Testing, App Store
