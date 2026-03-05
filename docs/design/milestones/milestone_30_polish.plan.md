# Milestone 30: Polish & Accessibility

## Status
Not Started

## Goal
Add micro-animations, haptic feedback, VoiceOver support, Dynamic Type support, and fix edge cases across the entire app.

## Dependencies
All previous iOS milestones (1-8, 21-29)

## Plan
- Animations: breathing timer, voice waveform, card transitions, confetti on completion
- Haptic feedback on button taps, session start/end, milestones, errors
- VoiceOver labels, hints, grouped elements, state change announcements
- Dynamic Type with scalable fonts, test at all sizes
- Dark mode verification and contrast (WCAG AA)
- Edge cases: low storage, expired auth, no internet, FamilyControls re-auth, calendar permission revoked
- Performance: Instruments profiling, LazyVStack optimization

## Key Files
| File | Description |
|------|-------------|
| Various | Animation modifiers, accessibility modifiers across the app |

## Implementation Details

1. **Animations**: Breathing animation on focus timer (scale + opacity oscillation), voice waveform bars during AI recording/playback, card enter/exit transitions (slide + fade), tab switch transitions, progress ring fill animation on habit completion, confetti/celebration on session completion, pull-to-refresh with custom animation.

2. **Haptic feedback**: UIImpactFeedbackGenerator on button taps (light), session start/end (medium), timer milestones (heavy), error states (notification).

3. **VoiceOver accessibility**: Add accessibility labels to all interactive elements, accessibility hints for complex interactions (e.g., "Double tap to start focus session"), group related elements with accessibilityElement(children: .combine), announce state changes (session started, AI response received).

4. **Dynamic Type**: All text uses scalable fonts (relativeTo:), test at all accessibility sizes, ensure layouts don't break at XXL sizes, use ScrollView where content might overflow.

5. **Dark mode**: Verify all screens in dark mode, ensure sufficient contrast ratios (WCAG AA), test custom colors in both modes.

6. **Edge cases**: Handle low storage (warn when SwiftData might fail), handle expired auth (redirect to sign-in), handle no internet gracefully (offline mode indicators), handle FamilyControls re-authorization needed, handle calendar permission revoked.

7. **Performance**: Profile with Instruments, optimize list rendering with LazyVStack, reduce unnecessary redraws.

## Testing
- VoiceOver can navigate entire app
- Dynamic Type renders correctly at all sizes
- Dark mode has no contrast issues
- Animations are smooth (60fps)
- Haptics fire at correct times
- Edge cases handled gracefully

## Notes
Duration: 3 days
