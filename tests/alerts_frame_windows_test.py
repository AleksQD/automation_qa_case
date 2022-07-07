import pytest

from ..pages.alerts_frame_windows_page import BrowserWindowsPage


# @pytest.mark.skip
class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_page = BrowserWindowsPage(
                driver, 'https://demoqa.com/browser-windows')
            browser_page.open()
            result = browser_page.check_oppened_new_tab_or_window('tab')
            assert result == 'This is a sample page', "The new tab has not oppend"

        def test_new_window(self, driver):
            browser_page = BrowserWindowsPage(
                driver, 'https://demoqa.com/browser-windows')
            browser_page.open()
            result = browser_page.check_oppened_new_tab_or_window('window')
            assert result == 'This is a sample page', "The new window has not oppend"
