import pytest

from ..pages.alerts_frame_windows_page import AlertsPage, BrowserWindowsPage, FramesPage


# @pytest.mark.skip
class TestAlertsFrameWindows:
    @pytest.mark.skip
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

    @pytest.mark.skip
    class TestAlerts:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(
                driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert did not show up"

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(
                driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(
                driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text, flag = alert_page.check_confirm_alert()
            alert_text = alert_text.split()[-1]
            assert alert_text == flag, "Alert did not show up"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(
                driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text, resut_text = alert_page.check_prompt_alert()
            resut_text = resut_text.split()[-1]
            assert alert_text == resut_text, "Alert did not show up"

    class TestFrames:

        def test_see_alert(self, driver):
            frame_page = FramesPage(
                driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page',
                                     '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page',
                                     '100px', '100px'], "The frame does not exist"
