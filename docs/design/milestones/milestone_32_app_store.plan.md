# Milestone 32: App Store Submission

## Status
Not Started

## Goal
Prepare all App Store assets, complete the listing, write privacy policy, apply for FamilyControls entitlement, and submit for App Store review.

## Dependencies
All previous milestones, Milestone 31 testing complete

## Plan
- App Store screenshots for required device sizes with marketing overlays
- 1024x1024 app icon following design language
- App Store listing: name, subtitle, description, keywords, category
- Privacy policy covering data collection, storage, third-parties, user rights
- FamilyControls entitlement application (submit early; may take weeks)
- App review preparation: demo account, review notes
- In-app purchases: StoreKit 2 for subscriptions
- Submit build for review

## Key Files
| File | Description |
|------|-------------|
| App Store Connect configuration | Listing metadata |
| privacy policy document | Hosted privacy policy |
| marketing assets | Screenshots, app icon |

## Implementation Details

1. **App Store screenshots**: Capture screenshots on iPhone 16 Pro Max (6.7") and iPhone SE (4.7") for required sizes. Screens: Home dashboard, AI voice chat, Active focus session, Calendar view, Widget showcase. Add marketing text overlays.

2. **App icon**: Design 1024x1024 app icon following design language (soft colors, rounded, recognizable at small sizes). Generate all required sizes via asset catalog.

3. **App Store listing**: App name ("BetterSelf" or final name), subtitle (e.g., "AI Focus & Calendar Assistant"), description (highlight both pillars: blocking + AI), keywords (productivity, focus, screen time, AI assistant, calendar, schedule), category: Productivity.

4. **Privacy policy**: Create privacy policy covering data collection (calendar, usage analytics, voice data), data storage (AWS), third-party services (Google Calendar, AWS), user rights (deletion, export). Host on a public URL.

5. **FamilyControls entitlement**: Submit request to Apple explaining app use case for FamilyControls (productivity app for self-management, NOT parental controls). Include screenshots of blocking UI. Explain accountability gatekeeper concept. This may require back-and-forth with Apple.

6. **App review preparation**: Ensure app passes Apple's guidelines (no private API use, proper permission descriptions, functional demo account for reviewers). Write App Review notes explaining FamilyControls usage. Provide demo credentials.

7. **In-app purchases**: Configure subscription products in App Store Connect (monthly + yearly premium). Implement StoreKit 2 for subscription management.

8. **Submit for review**: Build archive in Xcode, upload to App Store Connect, select build, submit for review.

## Testing
- All screenshots render correctly on all device sizes
- App icon looks good at all sizes
- Privacy policy URL loads
- Subscription flow works in sandbox
- Build uploads successfully
- App Store listing preview looks correct

## Notes
FamilyControls entitlement approval can take several weeks. Submit the entitlement request as early as possible (ideally during Phase A). If not approved by launch, ship without hard app blocking (use accountability/nudge mode) and add it via update once approved. Apple review typically takes 1-3 days but can take longer for apps using FamilyControls.

Duration: 3 days
