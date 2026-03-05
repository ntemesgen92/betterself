import SwiftUI

enum BSColors {
    static let primary = Color(hex: 0x5B8DEF)
    static let lavender = Color(hex: 0x9B8FE8)
    static let teal = Color(hex: 0x4ECDC4)

    static let backgroundLight = Color(hex: 0xF8F9FA)
    static let backgroundDark = Color(hex: 0x1A1B2E)
    static let surfaceDark = Color(hex: 0x2D2D3F)

    static let textPrimary = Color(hex: 0x1A1B2E)
    static let textSecondary = Color(hex: 0x6B7280)

    static var background: Color {
        Color(.systemBackground)
    }

    static var surface: Color {
        Color(.secondarySystemBackground)
    }

    static var cardBackground: Color {
        Color(.tertiarySystemBackground)
    }
}

extension Color {
    init(hex: UInt, opacity: Double = 1.0) {
        self.init(
            .sRGB,
            red: Double((hex >> 16) & 0xFF) / 255,
            green: Double((hex >> 8) & 0xFF) / 255,
            blue: Double(hex & 0xFF) / 255,
            opacity: opacity
        )
    }
}
