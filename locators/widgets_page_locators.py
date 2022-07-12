from selenium.webdriver.common.by import By

class AccordianPageLocators:
    FIRST_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD_ACCORDIAN_TITLE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')
