from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form filds

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:
    RADIO_LIST = (By.CSS_SELECTOR, 'input[type="radio"]+label')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebTablePageLocators:
    # add_person_form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROWS = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    # result
    MASSAGE_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    MASSAGE_RIGHT_CLICK = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    MASSAGE_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    # new tab links

    HOME_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DINAMIC_HOME_LINK = (By.CSS_SELECTOR, 'a[id="dinamikLink"]')

    # api call links

    CREATED_LINK = (By.CSS_SELECTOR, 'a[id="created"]')
    NO_CONTENT_LINK = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED_LINK = (By.CSS_SELECTOR, 'a[id="moved"]')
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN_LINK = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    NOT_FOUND_LINK = (By.CSS_SELECTOR, 'a[id="invalid-url"]')

    RESULT_STATUS_CODE = (By.XPATH, '//*[@id="linkResponse"]/b[1]')


class UploadDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')


class DynamicPropertiesPageLocators:
    COLOR_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
