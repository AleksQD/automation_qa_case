from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
	TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
	NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
	NEW_WINDOW_MESS_BUTTON = (
		By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

	TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
