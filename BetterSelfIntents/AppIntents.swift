import AppIntents

struct StartFocusIntent: AppIntent {
    static var title: LocalizedStringResource = "Start Focus Session"
    static var description = IntentDescription("Start a focus session with BetterSelf")

    func perform() async throws -> some IntentResult {
        .result()
    }
}
