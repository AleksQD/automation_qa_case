import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys


from ..generator.generator import generated_color, generated_date
from ..locators.widgets_page_locators import AccordianPageLocators, AutoComplitePageLocators, DatePickerPageLocators, MenuPageLocators, ProgressBarPageLocators, SelectMenuPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators
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


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_items = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_items:
            self.action_move_to_element(item)
            data.append(item.text)
        return data, len(menu_items)


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_menu(self):
        result = []
        check_result  = []
        colors = ['Voilet', 'Red', 'Blue', 'Green',
                  'Yellow', 'Purple', 'Black', 'White', 'Indigo', 'Magenta', 'Aqua']
        select_value = self.select_value_random_item(
            self.locators.SELECT_VALUE, self.locators.SELECT_VALUE_ITEMS)
        select_value_result = self.element_is_visible(self.locators.SELECT_VALUE_RESULT).text
        result.append(select_value)
        check_result.append(select_value_result)

        select_one = self.select_value_random_item(
            self.locators.SELECT_ONE, self.locators.SELECT_ONE_ITEMS)
        select_one_result = self.element_is_visible(
            self.locators.SELECT_ONE_RESULT).text
        result.append(select_one)
        check_result.append(select_one_result)
        
        random_color = random.choice(colors)
        select_old = self.element_is_visible(self.locators.SELECT_OLD)
        self.select_by_visible_text(select_old,random_color)
        select_old_result_list = self.select_all_selected_items(select_old)
        select_old_result = select_old_result_list[0].text
        result.append(random_color)
        check_result.append(select_old_result)

        multiselect_choice = self.multiselect_random_items(
            self.locators.MULTISELECT, self.locators.MULTISELECT_ITEMS)
        multiselect_select_items = self.elements_are_present(self.locators.MULTISELECT_RESULT)
        multiselect_result = [item.text for item in multiselect_select_items]
        result.append(multiselect_choice)
        check_result.append(multiselect_result)
        
        multiselect_old_choice, multiselect_old_result = self.multiselect_old_random_items(
            self.locators.MULTISELECT_OLD)
        result.append(multiselect_old_choice)
        check_result.append(multiselect_old_result)
        
        return result, check_result


    def select_value_random_item(self, select_locator, items_locator):        
        self.element_is_visible(select_locator).click()
        values = self.elements_are_present(items_locator)
        value = random.choice(values)
        self.go_to_element(value)
        result = value.text
        value.click()
        return result

    def multiselect_random_items(self, select_locators, items_locator):
        data = []
        select = self.element_is_visible(select_locators)
        select.click()
        values = self.elements_are_present(items_locator)
        for i in range(0, random.randrange(1, len(values))):
            self.go_to_element(values[i])
            result = values[i].text
            data.append(result)
            values[i].click()
        select.click()
        return data

    def multiselect_old_random_items(self, select_locators):
        select_list = []
        select = self.element_is_visible(select_locators)
        item_list = self.select_options(select)        
        for i in range(0, random.randrange(1, len(item_list))):
            select_list.append(item_list[i].text)
            self.select_by_visible_text(select, item_list[i].text)        
        result_list = self.select_all_selected_items(select)
        result_list = [item.text for item in result_list]

        return select_list, result_list