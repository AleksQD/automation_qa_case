import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys


from ..generator.generator import generated_color
from ..locators.widgets_page_locators import AccordianPageLocators, AutoComplitePageLocators
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
		colors = random.sample(next(generated_color()).color_name, k=random.randint(2,5))
		for color in colors:
			input = self.element_is_visible(self.locators.MULTIPLE_INPUT)
			input.send_keys(color)
			input.send_keys(Keys.ENTER)
		return colors

	def remove_value_from_multy(self):
		count_value_before = len(
			self.elements_are_present(self.locators.MULTIPLE_VALUE))
		remove_buttons_list = self.elements_are_visible(self.locators.MULTIPLE_VALUE_REMOVE)
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
