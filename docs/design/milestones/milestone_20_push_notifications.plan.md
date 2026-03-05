# Milestone 20: Push Notifications

## Status
Not Started

## Goal
Set up AWS SNS for push notifications via APNs, implement daily briefing scheduler, focus session reminders, and schedule alerts. Users can register device tokens and customize notification preferences.

## Dependencies
Milestones 12 (Lambda API), 14 (User & Auth API), 17 (AI Secretary API)

## Plan
- Create SNS platform application for APNs
- Implement device registration and preferences endpoints
- Build notification service with send_push helper
- Add EventBridge rules for scheduled notifications (briefing, focus reminders)
- Implement event reminders and AI nudges

## Key Files
| File | Description |
|------|-------------|
| api/services/notification_service.py | SNS send_push, scheduled notification logic |
| infrastructure/stacks/notifications_stack.py | SNS platform app, topics, EventBridge rules |
| api/routers/notifications.py | Device registration, preferences endpoints |

## Implementation Details

1. **CDK**: Create SNS platform application for APNs (requires Apple Push certificate or key), create SNS topics for different notification types

2. **POST /notifications/register**: Register device token from iOS (creates SNS platform endpoint)

3. **PUT /notifications/preferences**: Update notification preferences (which types to receive)

4. **notification_service.py**: send_push() helper that publishes to SNS endpoint with APNs payload

5. **Daily briefing scheduler**: EventBridge rule triggers Lambda at user's preferred time (default 7am), Lambda generates briefing and sends push with summary

6. **Focus session reminders**: When a scheduled focus session is approaching (15 min before), send reminder push

7. **Calendar event reminders**: Send push N minutes before events (user-configurable)

8. **AI nudges**: Periodic encouragement pushes (e.g., "You've been focused for 2 hours — time for a break!")

9. **Notification payload**: Include title, body, category (for actionable notifications), deep link URL

## Testing
- Device registration creates SNS endpoint
- Push notification received on device
- Daily briefing fires at correct time
- Focus reminders arrive before sessions
- Notification preferences are respected

## Notes
- Requires Apple Developer account with push notification certificate/key
- APNs sandbox for development, production for TestFlight/App Store
- **Duration**: 2 days
