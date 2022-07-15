from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        # self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView;", element)

    def select_by_value(self, element, value):
        return Select(element).select_by_value(value)

    def select_by_visible_text(self, element, value):
        return Select(element).select_by_visible_text(value)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_move, y_move):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, x_move, y_move)
        actions.perform()

    def action_move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element,0,0)
        actions.perform()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def switch_to_frame(self, web_element):
        return self.driver.switch_to.frame(web_element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
