import XCTest
@testable import BetterSelf

final class BetterSelfTests: XCTestCase {
    func testColorsExist() {
        XCTAssertNotNil(BSColors.primary)
        XCTAssertNotNil(BSColors.lavender)
        XCTAssertNotNil(BSColors.teal)
    }

    func testThemeConstants() {
        XCTAssertGreaterThan(BSTheme.cornerRadiusLarge, 0)
        XCTAssertGreaterThan(BSTheme.paddingMedium, 0)
    }
}
