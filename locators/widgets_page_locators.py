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
	SINGLE_VALUE = (
		By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
	DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
	DATE_SELECT_MONTH = (
		By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
	DATE_SELECT_YEAR = (
		By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
	DATE_SELECT_DAY_LIST = (
		By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

	DATE_AND_TIME_INPUT = (
		By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
	DATE_AND_TIME_SELECT_MONTH = (
		By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
	DATE_AND_TIME_SELECT_MONTH_LIST = (
		By.CSS_SELECTOR, 'div[class*="react-datepicker__month-option"]')
	DATE_AND_TIME_SELECT_YEAR = (
		By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
	DATE_AND_TIME_SELECT_YEAR_LIST = (
		By.CSS_SELECTOR, 'div[class^="react-datepicker__year-option"]')
	DATE_AND_TIME_SELECT_DAY_LIST = (
		By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
	DATE_AND_TIME_SELECT_TIME_LIST = (
		By.CSS_SELECTOR, 'li[class*="react-datepicker__time-list-item "]')


class SliderPageLocators:
	SLIDER_INPUT = (
		By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
	SLIDER_INPUT_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
	PROGRESS_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
	PROGRESS_VALUE = (By.CSS_SELECTOR, 'div[id="progressBar"] div')
