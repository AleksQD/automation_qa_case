from selenium.webdriver.common.by import By


class AccordianPageLocators:
	FIRST_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
	FIRST_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
	SECOND_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
	SECOND_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
	THIRD_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
	THIRD_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoComplitePageLocators:
	MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
	MULTIPLE_VALUE = (
		By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
	MULTIPLE_VALUE_REMOVE = (
		By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
	SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
	SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
