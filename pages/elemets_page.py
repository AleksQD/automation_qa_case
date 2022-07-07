
import base64
import os
import random
import time
import requests


from ..generator.generator import generated_file, generated_person
from ..locators.elemets_page_locators import ButtonsPageLocators, CheckBoxPageLocators, DynamicPropertiesPageLocators, LinksPageLocators, RadioButtonPageLocators, TextBoxPageLocators, UploadDownloadPageLocators, WebTablePageLocators
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        curr_address = person_info.current_address
        perm_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(
            self.locators.CURRENT_ADDRESS).send_keys(curr_address)
        self.element_is_visible(
            self.locators.PERMANENT_ADDRESS).send_keys(perm_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, curr_address, perm_address

    def check_filled_form(self):
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(
            self.locators.CREATED_EMAIL).text.split(':')[1]
        curr_addr = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        perm_addr = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, curr_addr, perm_addr


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_random_radio_button(self):
        item_list = self.elements_are_present(self.locators.RADIO_LIST)
        item = item_list[random.randint(0, 2)]
        item.click()
        return item.text

    def get_output_result(self):
        result = self.element_is_present(self.locators.OUTPUT_RESULT)
        return result.text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(
                self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(
                self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(
                self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(
                self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            count_row_button = self.element_is_visible(
                self.locators.COUNT_ROWS)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.select_by_value(count_row_button, str(i))
            data.append(self.check_rows_count())
        return data

    def check_rows_count(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_on_button(self):
        self.action_double_click(self.element_is_visible(
            self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_on_button(self.locators.MASSAGE_DOUBLE_CLICK)

    def right_click_on_button(self):
        self.action_right_click(self.element_is_visible(
            self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_button(self.locators.MASSAGE_RIGHT_CLICK)

    def one_click_on_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_button(self.locators.MASSAGE_CLICK_ME)

    def check_clicked_on_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_new_tab()
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_status_code_link(self, url):
        request = requests.get(url)
        return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.element_is_present(
            self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'G:\Projects\automation_QA\automation_qa_case\data\filetest{random.randint(0,999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_chenged_of_color(self):
        color_button = self.element_is_visible(self.locators.COLOR_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON, 6)
        except TimeoutException:
            return False
        return True
