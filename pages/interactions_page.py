import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys

from ..locators.interactions_page_locators import SortablePageLocators
from .base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def change_list_order(self):
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEMS)
        self.change_order_itams(self.locators.LIST_ITEMS)
        order_after = self.get_sortable_items(self.locators.LIST_ITEMS)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEMS)
        self.change_order_itams(self.locators.GRID_ITEMS)
        order_after = self.get_sortable_items(self.locators.GRID_ITEMS)
        return order_before, order_after
    
    def change_order_itams(self, items_locator):
        item_list = random.sample(
            self.elements_are_visible(items_locator), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_elements(item_what, item_where)

    def get_sortable_items(self, elemets):
        item_list = self.elements_are_visible(elemets)
        return [item.text for item in item_list]
