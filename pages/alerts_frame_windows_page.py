import os
import random
import time
from selenium.webdriver import Keys
from ..generator.generator import generated_file, generated_person
from ..locators.alerts_frame_windows_page_locators import AlertsPageLocators, BrowserWindowsPageLocators
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


class AlertsPage(BasePage):
	locators = AlertsPageLocators()

	def check_see_alert(self):
		self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
		alert = self.switch_to_alert()
		return alert.text

	def check_alert_appear_5_sec(self):
		self.element_is_visible(self.locators.ALERT_AFTER_FIVE_SEC_BUTTON).click()
		time.sleep(5)
		alert = self.switch_to_alert()
		return alert.text

	def check_confirm_alert(self):
		self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
		alert = self.switch_to_alert()
		rand = random.randrange(2)
		if rand == 0:
			alert.dismiss()
			flag = 'Cancel'
		else:
			alert.accept()
			flag = 'Ok'
		text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
		return text_result, flag

	def check_prompt_alert(self):
		text = f'autotest{random.randint(0,999)}'
		self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
		alert = self.switch_to_alert()
		alert.send_keys(text)
		alert.accept()
		text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
		return text, text_result
