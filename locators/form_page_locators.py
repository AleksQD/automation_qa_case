from selenium.webdriver.common.by import By


class FormPageLocators:
    # form
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER_RADIO_LIST = (By.CSS_SELECTOR, 'input[type="radio"]+label')
    HOBBIES_CHECKBOX_LIST = (
        By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div/label')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    UPLOAD_PICTURE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table result
    RESULT_TABLE = (By.CSS_SELECTOR, 'table tbody td:last-child')
