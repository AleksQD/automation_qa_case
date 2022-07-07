

import os
import random
from selenium.webdriver import Keys
from ..generator.generator import generated_file, generated_person
from ..locators.form_page_locators import FormPageLocators
from .base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        first_name = person.firstname
        last_name = person.lastname
        email = person.email
        mobile = person.mobile
        current_address = person.current_address
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.click_random_gender_radio_button()
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(
        self.random_subject_return())
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.click_random_hobbies_checkbox()
        self.upload_picture_file(path)
        self.element_is_visible(
            self.locators.CURRENT_ADDRESS).send_keys(current_address)
        state, city = self.random_state_and_city_return()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        date = []
        for item in result_list:
            self.go_to_element(item)
            date.append(item.text)
        
        return date

    def click_random_hobbies_checkbox(self):
        item_list = self.elements_are_visible(
            self.locators.HOBBIES_CHECKBOX_LIST)
        count = 5
        while count != 0:
            item = item_list[random.randint(0, 2)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def click_random_gender_radio_button(self):
        item_list = self.elements_are_present(self.locators.GENDER_RADIO_LIST)
        item = item_list[random.randint(0, 2)]
        item.click()

    def upload_picture_file(self, path):
        self.element_is_present(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)

    def random_subject_return(self):
        list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
                "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
        return list[random.randint(0, len(list)-1)]

    def random_state_and_city_return(self):
        states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
        cities_in_state = {"NCR": ["Delhi", "Gurgaon", "Noida"],  "Uttar Pradesh": [
            "Agra", "Lucknow", "Merrut"], "Haryana": ["Karnal", "Panipat"], "Rajasthan": ["Jaipur", "Jaiselmer"]}

        state = states[random.randint(0, len(states)-1)]
        cities = cities_in_state.get(state)
        city = cities[random.randint(0, len(cities)-1)]
        return state,city
