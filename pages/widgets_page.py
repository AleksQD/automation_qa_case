from selenium.common.exceptions import TimeoutException
import time

from ..locators.widgets_page_locators import AccordianPageLocators
from .base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian_text(self, number):
        accordian = {
            'first': {
                'title': self.locators.FIRST_ACCORDIAN_TITLE,
                'text': self.locators.FIRST_ACCORDIAN_TEXT
            },
            'second': {
                'title': self.locators.SECOND_ACCORDIAN_TITLE,
                'text': self.locators.SECOND_ACCORDIAN_TEXT
            },
            'third': {
                'title': self.locators.THIRD_ACCORDIAN_TITLE,
                'text': self.locators.THIRD_ACCORDIAN_TEXT
            }
        }

        section_title = self.element_is_visible(accordian[number]['title'])
        section_title.click()
        try:
            section_text = self.element_is_visible(
                accordian[number]['text']).text
        except TimeoutException:
            section_title.click()
            section_text = self.element_is_visible(
                accordian[number]['text']).text
        return [section_title.text, len(section_text)]
