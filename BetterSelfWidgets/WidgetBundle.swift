import WidgetKit
import SwiftUI

@main
struct BetterSelfWidgetBundle: WidgetBundle {
    var body: some Widget {
        FocusTimerWidget()
    }
}

struct FocusTimerWidget: Widget {
    let kind: String = "FocusTimerWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: FocusTimerProvider()) { entry in
            Text("Focus Timer")
        }
        .configurationDisplayName("Focus Timer")
        .description("Shows your active focus session.")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}

struct FocusTimerEntry: TimelineEntry {
    let date: Date
}

struct FocusTimerProvider: TimelineProvider {
    func placeholder(in context: Context) -> FocusTimerEntry {
        FocusTimerEntry(date: .now)
    }

    func getSnapshot(in context: Context, completion: @escaping (FocusTimerEntry) -> Void) {
        completion(FocusTimerEntry(date: .now))
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<FocusTimerEntry>) -> Void) {
        let entry = FocusTimerEntry(date: .now)
        let timeline = Timeline(entries: [entry], policy: .after(.now.addingTimeInterval(60)))
        completion(timeline)
    }
}
