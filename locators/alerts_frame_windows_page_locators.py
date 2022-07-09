from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESS_BUTTON = (
        By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

    TITLE_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    ALERT_AFTER_FIVE_SEC_BUTTON = (
        By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')
