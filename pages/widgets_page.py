import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys


from ..generator.generator import generated_color, generated_date
from ..locators.widgets_page_locators import AccordianPageLocators, AutoComplitePageLocators, DatePickerPageLocators, ProgressBarPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators
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


class AutoComplitePage(BasePage):
    locators = AutoComplitePageLocators()

    def fill_autocomplite_multiple_input(self):
        colors = random.sample(
            next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input = self.element_is_visible(self.locators.MULTIPLE_INPUT)
            input.send_keys(color)
            input.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multy(self):
        count_value_before = len(
            self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_buttons_list = self.elements_are_visible(
            self.locators.MULTIPLE_VALUE_REMOVE)
        for value in remove_buttons_list:
            value.click()
            break
        count_value_after = len(
            self.elements_are_present(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_colors_in_input_multy(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_autocomplite_single_input(self):
        color = random.sample(
            next(generated_color()).color_name, k=1)
        input = self.element_is_visible(self.locators.SINGLE_INPUT)
        input.send_keys(color)
        input.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_input_single(self):
        color = self.element_is_present(self.locators.SINGLE_VALUE).text
        return color


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_by_visible_text(self.element_is_present(
            self.locators.DATE_SELECT_MONTH), date.month)
        self.select_by_visible_text(self.element_is_present(
            self.locators.DATE_SELECT_YEAR), date.year)
        self.set_date_item_from_list(
            self.locators.DATE_SELECT_DAY_LIST, date.day)
        time.sleep(2)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_present(
            self.locators.DATE_AND_TIME_SELECT_MONTH).click()
        self.set_element_in_list(
            self.locators.DATE_AND_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_present(
            self.locators.DATE_AND_TIME_SELECT_YEAR).click()
        self.set_element_in_list(
            self.locators.DATE_AND_TIME_SELECT_YEAR_LIST, '2022')
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_SELECT_DAY_LIST, date.day)
        self.set_element_in_list(
            self.locators.DATE_AND_TIME_SELECT_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_item_from_list(self, element, value):
        item_list = self.elements_are_present(element)
        if int(value) < 10:
            value = value[1]
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def set_element_in_list(self, element, value):
        list_item = self.elements_are_present(element)
        for item in list_item:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_slider(self):
        value_before = self.element_is_visible(
            self.locators.SLIDER_INPUT_VALUE).get_attribute('value')
        input = self.element_is_present(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(input, random.randint(0, 350), 0)
        value_after = self.element_is_visible(
            self.locators.SLIDER_INPUT_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def check_progress(self):
        progress_button = self.element_is_visible(
            self.locators.PROGRESS_BUTTON)
        progress_button.click()
        time.sleep(random.randint(0, 14))
        progress_button.click()
        result = self.element_is_present(self.locators.PROGRESS_VALUE).text
        return int(result.replace('%', ''))


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tabs_name):
        tabs_dict = {'What': {'title': self.locators.TAB_TITLE_WHAT,
                              'content': self.locators.TAB_TEXT_WHAT},
                     'Origin': {'title': self.locators.TAB_TITLE_ORIGIN, 'content': self.locators.TAB_TEXT_ORIGIN},
                     'Use': {'title': self.locators.TAB_TITLE_USE, 'content': self.locators.TAB_TEXT_USE},
                     'More': {'title': self.locators.TAB_TITLE_USE, 'content': self.locators.TAB_TEXT_USE}
                     }
        try:
            self.element_is_visible(tabs_dict[tabs_name]['title']).click()
            tabs_title = self.element_is_visible(
                tabs_dict[tabs_name]['title']).text
            tabs_text = self.element_is_visible(
                tabs_dict[tabs_name]['content']).text
        except Exception:
            tabs_title, tabs_text = '', ''
            return tabs_title, tabs_text
        return tabs_title, tabs_text


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        time.sleep(1)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(
            self.locators.BUTTON, self.locators.BUTTON_TOOL_TIPS)
        tool_tip_text_field = self.get_text_from_tool_tips(
            self.locators.FIELD, self.locators.FIELD_TOOL_TIPS)
        tool_tip_text_contrary = self.get_text_from_tool_tips(
            self.locators.CONTRARY_LINKS, self.locators.CONTRARY_LINKS_TOOL_TIPS)
        tool_tip_text_section = self.get_text_from_tool_tips(
            self.locators.SECTION_LINKS, self.locators.SECTION_LINKS_TOOL_TIPS)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
