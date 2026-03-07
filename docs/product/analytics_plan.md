# BetterSelf -- Product Analytics & KPI Plan

> **Author:** Dev A
> **Status:** Draft
> **Purpose:** Define what we measure, why, and how. This drives data-informed product decisions.

---

## North Star Metric

**Weekly Active Focus Hours** -- total hours users spend in focus sessions per week. This captures both retention (users come back) and value delivery (they're actually using the core feature).

---

## KPI Framework

### Acquisition
| Metric | Definition | Target (Month 1) | Tool |
|--------|-----------|-------------------|------|
| App Store impressions | Times listing is viewed | [Research] | App Store Connect |
| Download rate | Downloads / impressions | >5% | App Store Connect |
| Install-to-onboarding-complete | % of installs that finish onboarding | >60% | Pinpoint |

### Activation
| Metric | Definition | Target | Tool |
|--------|-----------|--------|------|
| Time to first focus session | Minutes from install to first session | <10 min | Pinpoint |
| Time to first AI interaction | Minutes from install to first AI chat | <15 min | Pinpoint |
| Onboarding completion rate | % who complete all onboarding steps | >70% | Pinpoint |
| Calendar connected rate | % who connect Apple or Google Calendar | >50% | Pinpoint |

### Engagement
| Metric | Definition | Target | Tool |
|--------|-----------|--------|------|
| DAU / MAU ratio | Daily active / monthly active | >30% | Pinpoint |
| Avg focus sessions per user/week | [Self-explanatory] | 5+ | Backend logs |
| Avg AI queries per user/day | [Self-explanatory] | 3+ | Backend logs |
| Daily briefing open rate | Push opened / push sent | >40% | Pinpoint + SNS |
| Habit check-in rate | Check-ins / habits due | >60% | Backend logs |

### Retention
| Metric | Definition | Target | Tool |
|--------|-----------|--------|------|
| Day 1 retention | % return day after install | >50% | Pinpoint |
| Day 7 retention | % return 7 days after install | >35% | Pinpoint |
| Day 30 retention | % return 30 days after install | >20% | Pinpoint |
| Churn rate | % who stop using for 14+ days | <15%/mo | Pinpoint |

### Revenue
| Metric | Definition | Target | Tool |
|--------|-----------|--------|------|
| Free-to-premium conversion | % who upgrade | >3% | StoreKit + Pinpoint |
| Premium retention (monthly) | % who renew | >80% | App Store Connect |
| ARPU | Average revenue per user | [TBD] | App Store Connect |
| LTV | Lifetime value | [TBD] | Calculated |

### AI-Specific Metrics
| Metric | Definition | Target | Tool |
|--------|-----------|--------|------|
| AI action confirmation rate | confirmed / total proposed | >75% | Backend logs |
| AI retry rate | Rephrased messages / total messages | <15% | Backend logs |
| Gatekeeper override rate | Overrides approved / total requests | 20-40% | Backend logs |
| AI cost per user/month | Bedrock token cost per active user | <$0.50 | CloudWatch |

---

## Pinpoint Event Taxonomy

[Define every event we track in AWS Pinpoint]

| Event Name | Trigger | Properties |
|------------|---------|-----------|
| `onboarding_started` | User opens app first time | -- |
| `onboarding_step_completed` | Each onboarding step | `step_name`, `step_number` |
| `onboarding_completed` | Final step done | `goals_selected`, `calendar_connected` |
| `focus_session_started` | Session begins | `profile_id`, `mode`, `duration_planned` |
| `focus_session_completed` | Session ends naturally | `duration_actual`, `blocked_attempts` |
| `focus_session_overridden` | User ends session early | `duration_actual`, `gatekeeper_approved` |
| `ai_message_sent` | User sends AI message | `input_method` (voice/text), `tier` |
| `ai_action_proposed` | AI proposes an action | `action_type` |
| `ai_action_confirmed` | User confirms | `action_type` |
| `ai_action_rejected` | User rejects | `action_type` |
| `calendar_event_created` | New event | `source` (manual/ai), `calendar` |
| `task_created` | New task | `priority`, `has_due_date` |
| `habit_checkin` | Habit checked in | `habit_id`, `streak_length` |
| `daily_briefing_opened` | Briefing viewed | `opened_from` (push/app) |
| `premium_upgrade_tapped` | CTA tapped | `source_screen` |
| `premium_purchased` | Subscription started | `plan` (monthly/yearly) |

---

## Dashboard Specifications

### Daily Operations Dashboard (CloudWatch)
[Define what the daily monitoring dashboard shows]

### Weekly Product Review Dashboard
[Define what the PM reviews weekly]

### Monthly Business Review
[Define what goes into the monthly stakeholder report]

---

## Review Cadence

- **Daily:** Dev B checks CloudWatch operational metrics (errors, latency)
- **Weekly:** Dev A reviews product metrics in Pinpoint, writes 1-paragraph summary
- **Monthly:** Both review all KPIs, identify trends, prioritize backlog based on data
- **Quarterly:** Comprehensive product review with updated targets
