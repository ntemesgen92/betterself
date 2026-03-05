# Milestone 1: Project Setup

## Status
Not Started

## Goal
Initialize the Xcode project with SwiftUI lifecycle, configure Swift package dependencies, establish a clean folder structure, and create a design system foundation (colors, typography, reusable components). Set up CI with Xcode Cloud for automated builds and testing.

## Dependencies
None

## Plan
- Create Xcode project with SwiftUI lifecycle
- Add Swift Package dependencies (Alamofire, KeychainAccess)
- Establish folder structure: App/, Core/Design/, Core/Models/, Core/Services/, Core/Storage/, Features/, Extensions/
- Implement design system: Headspace-inspired palette, SF Pro Rounded typography, reusable card/button components
- Configure build schemes (Debug/Release)
- Set up Xcode Cloud for CI

## Key Files
| File | Description |
|------|-------------|
| BetterSelfApp.swift | App entry point, SwiftUI lifecycle |
| ContentView.swift | Root view (placeholder until tab navigation) |
| Theme.swift | Design system configuration |
| Colors.swift | Color palette definitions |
| Typography.swift | Font scale and text styles |
| Package.swift / SPM config | Alamofire, KeychainAccess dependencies |

## Implementation Details

1. **Xcode Project Setup**
   - Create new iOS app project with SwiftUI lifecycle (not UIKit/Storyboard)
   - Set minimum deployment target (e.g., iOS 17+)
   - Configure app display name, bundle ID, team, and signing

2. **Swift Package Dependencies**
   - Add Alamofire for networking (future API calls)
   - Add KeychainAccess for secure token storage

3. **Folder Structure**
   - `App/` - App entry, scene delegates
   - `Core/Design/` - Theme, Colors, Typography, reusable UI components
   - `Core/Models/` - Data model types
   - `Core/Services/` - Business logic and API services
   - `Core/Storage/` - Persistence and keychain
   - `Features/` - Feature-specific views and view models
   - `Extensions/` - Swift extensions

4. **Design System**
   - **Colors**: Headspace-inspired palette
     - Primary blue: `#5B8DEF`
     - Lavender: `#9B8FE8`
     - Teal: `#4ECDC4`
     - Light background: `#F8F9FA`
     - Dark background: `#1A1B2E`
   - **Typography**: SF Pro Rounded scale (title, headline, body, caption)
   - **Components**: Reusable CardView, PrimaryButton, SecondaryButton with design tokens

5. **Build Configuration**
   - Configure Debug scheme for development
   - Configure Release scheme for distribution

6. **Xcode Cloud CI**
   - Enable Xcode Cloud in App Store Connect
   - Configure workflow for build on commit/PR
   - Add test targets for future unit/UI tests

## Testing
- Project builds cleanly for both Debug and Release
- Design system preview renders correctly in Xcode canvas
- No build warnings from Swift packages

## Notes
- Duration: 3 days
