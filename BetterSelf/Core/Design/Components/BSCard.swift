import SwiftUI

struct BSCard<Content: View>: View {
    let content: Content

    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        content
            .padding(BSTheme.paddingMedium)
            .background(BSColors.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: BSTheme.cornerRadiusLarge))
            .shadow(
                color: .black.opacity(BSTheme.shadowOpacity),
                radius: BSTheme.shadowRadius,
                y: BSTheme.shadowY
            )
    }
}

struct BSPrimaryButton: View {
    let title: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(BSTypography.headline)
                .foregroundStyle(.white)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 14)
                .background(BSColors.primary)
                .clipShape(RoundedRectangle(cornerRadius: BSTheme.cornerRadiusMedium))
        }
    }
}

struct BSSecondaryButton: View {
    let title: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(BSTypography.headline)
                .foregroundStyle(BSColors.primary)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 14)
                .background(BSColors.primary.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: BSTheme.cornerRadiusMedium))
        }
    }
}
