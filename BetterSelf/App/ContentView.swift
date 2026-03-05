import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            HomeView()
                .tabItem {
                    Label("Home", systemImage: "house.fill")
                }

            FocusHomeView()
                .tabItem {
                    Label("Focus", systemImage: "moon.fill")
                }

            CalendarTabView()
                .tabItem {
                    Label("Calendar", systemImage: "calendar")
                }
        }
        .tint(BSColors.primary)
    }
}

// MARK: - Placeholder views (to be replaced in their respective milestones)

struct HomeView: View {
    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 20) {
                    Text("Good morning")
                        .font(BSTypography.title)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(.horizontal)

                    Text("Your AI productivity partner")
                        .font(BSTypography.body)
                        .foregroundStyle(.secondary)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(.horizontal)
                }
                .padding(.top)
            }
            .navigationTitle("BetterSelf")
        }
    }
}

struct FocusHomeView: View {
    var body: some View {
        NavigationStack {
            Text("Focus")
                .font(BSTypography.title)
                .navigationTitle("Focus")
        }
    }
}

struct CalendarTabView: View {
    var body: some View {
        NavigationStack {
            Text("Calendar")
                .font(BSTypography.title)
                .navigationTitle("Calendar")
        }
    }
}

#Preview {
    ContentView()
}
