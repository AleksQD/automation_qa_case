import os
import random
from selenium.webdriver import Keys
from ..generator.generator import generated_file, generated_person
from ..locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from .base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_oppened_new_tab_or_window(self, flag):
        if flag == 'tab':
            self.element_is_visible(self.locators.TAB_BUTTON).click()
        elif flag == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()

        else:
            return "invalid or empty flag is used"
        self.switch_to_new_tab()
        text_title = self.element_is_present(
            self.locators.TITLE_NEW_TAB).text
        return text_title
