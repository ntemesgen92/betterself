# Milestone 5: FamilyControls Integration

## Status
Not Started

## Goal
Integrate Apple's FamilyControls, ManagedSettings, and DeviceActivity frameworks to enable real app blocking, custom shield screens, and schedule-based monitoring. Replace mock blocking with actual device enforcement.

## Dependencies
- Milestone 1 (Project Setup)
- Milestone 4 (Focus Mode UI)

## Plan
- Request FamilyControls entitlement from Apple Developer portal
- Add FamilyControls, ManagedSettings, DeviceActivity frameworks
- Implement authorization flow and BlockingService
- Wire FamilyActivityPicker into AppPickerView
- Create ShieldConfiguration and DeviceActivityMonitor extensions
- Implement AI gatekeeper override flow (local heuristics for now)

## Key Files
| File | Description |
|------|-------------|
| BlockingService.swift | Authorization, shield application, schedule coordination |
| DeviceActivityMonitorExtension.swift | Schedule-based auto-start/stop |
| ShieldConfigurationExtension.swift | Custom blocked-app screen |
| ShieldActionExtension.swift | Override button handling |
| AppPickerView.swift | Integration with FamilyActivityPicker |

## Implementation Details

1. **Entitlement**
   - Request FamilyControls capability from Apple Developer portal
   - Add capability to Xcode project
   - Note: Apply early—approval can take time

2. **Frameworks**
   - Add FamilyControls, ManagedSettings, DeviceActivity to project

3. **BlockingService**
   - Call `AuthorizationCenter.shared.requestAuthorization()` for FamilyControls
   - Present system authorization UI (parent/guardian flow)
   - Store authorization state, handle re-request on reinstall
   - Use ManagedSettingsStore to apply/remove shields for selected applications and categories

4. **AppPickerView**
   - Replace placeholder with real FamilyActivityPicker
   - Bind selection to BlockingProfile.appSelections (FamilyActivitySelection)
   - Persist selection for profile save

5. **DeviceActivityMonitor Extension**
   - Create extension target for schedule-based blocking
   - Monitor events: session start at configured time, session end
   - Coordinate with BlockingService to apply/remove shields on schedule

6. **ShieldConfiguration Extension**
   - Custom shield when user opens blocked app
   - BetterSelf-branded message with current session timer
   - Use design system colors (teal, lavender)

7. **ShieldAction Extension**
   - When user taps override on shield, present AI challenge screen
   - Evaluate override reason via local heuristics (keyword matching, intent detection)
   - Full AI backend integration comes later
   - Allow/deny with feedback message

8. **Edge Cases**
   - Re-authorization after app reinstall: detect and prompt
   - Child vs individual mode: support both flows per FamilyControls docs
   - Handle authorization revoked (e.g., Screen Time settings change)

## Testing
- FamilyControls authorization flow works on real device
- Selected apps are shielded when session is active
- Schedule-based blocking starts and stops at configured times
- Shield customization renders correctly (branding, timer)
- Override flow presents challenge and responds to input
- Re-authorization prompt appears when needed

## Notes
- FamilyControls **cannot** be tested in the simulator—must use a physical device
- Apply for entitlement ASAP; build nudge/accountability fallback UI if entitlement is delayed
- Duration: 5 days
