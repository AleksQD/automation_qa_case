import random
import re
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys

from ..locators.interactions_page_locators import ResizablePageLocators, SelectablePageLocators, SortablePageLocators
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


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_select_list(self):
        self.element_is_visible(self.locators.LIST).click()
        self.click_random_element(self.locators.LIST_ITEMS)
        items_active = self.elements_are_visible(
            self.locators.LIST_ITEMS_ACTIVE)
        return len(items_active)

    def check_select_grid(self):
        self.element_is_visible(self.locators.GRID).click()
        self.click_random_element(self.locators.GRID_ITEMS)
        items_active = self.elements_are_visible(
            self.locators.GRID_ITEMS_ACTIVE)
        return len(items_active)

    def click_random_element(self, elemets_locator):
        item_list = random.sample(
            self.elements_are_visible(elemets_locator), k=2)
        [item.click() for item in item_list]


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self,value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self,element):
        element = self.element_is_present(element)
        size = element.get_attribute('style')
        return size

    def chenge_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def chenge_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(0, 300), random.randint(0, 200))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size