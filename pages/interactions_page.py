import random
import time

from ..locators.interactions_page_locators import DragblePageLocators, DroppablePageLocator, ResizablePageLocators, SelectablePageLocators, SortablePageLocators
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

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        element = self.element_is_present(element)
        size = element.get_attribute('style')
        return size

    def chenge_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def chenge_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(0, 300), random.randint(0, 200))
        max_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocator()

    def check_simple_drop(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag = self.element_is_visible(self.locators.SIMPLE_DRAG)
        drop = self.element_is_visible(self.locators.SIMPLE_DROP)
        self.action_drag_and_drop_to_elements(drag, drop)
        result = drop.text
        return result

    def check_accept_drop(self, accept_tipe):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drop = self.element_is_visible(self.locators.ACCEPT_DROP)
        if accept_tipe == 'not_accept':
            drag = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
            self.action_drag_and_drop_to_elements(drag, drop)
            result = drop.text
        if accept_tipe == 'accept':
            drag = self.element_is_visible(
                self.locators.ACCEPTABLE)
            self.action_drag_and_drop_to_elements(drag, drop)
            result = drop.text
        return result

    def check_prevent_propogation(self, greedy_tipe):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag = self.element_is_visible(self.locators.PREVENT_DRAG)
        if greedy_tipe == 'not_greedy':
            drop = self.element_is_visible(self.locators.NOTGREEDY_INN_BOX)
            self.action_drag_and_drop_to_elements(drag, drop)
            result = self.element_is_visible(
                self.locators.NOTGREEDY_OUT_BOX).text
        if greedy_tipe == 'greedy':
            drop = self.element_is_visible(self.locators.GREEDY_INN_BOX)
            self.action_drag_and_drop_to_elements(drag, drop)
            result = self.element_is_visible(
                self.locators.GREEDY_OUT_BOX).text
        return result.splitlines()

    def check_revert(self, drag_tipe):
        drags = {
            'revert': self.locators.WILL_REVERT,
            'not_revert': self.locators.NOT_REVERT
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drop = self.element_is_visible(self.locators.REVERT_DROP)
        drag = self.element_is_visible(drags[drag_tipe])
        self.action_drag_and_drop_to_elements(drag, drop)
        after_move_posicion = self.get_px_from_style_left_top(
            self.get_posicion_from_style(drag))
        time.sleep(1)
        after_revert_posicion = self.get_px_from_style_left_top(
            self.get_posicion_from_style(drag))
        return after_move_posicion, after_revert_posicion

    def get_px_from_style_left_top(self, value_of_size):
        left = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        top = value_of_size.split(';')[2].split(':')[1].replace(' ', '')
        return left, top




class DragblePage(BasePage):
    locators = DragblePageLocators()

    def get_before_and_after_posicion(self,drag_element, max_x=50, max_y=50):
        self.action_drag_and_drop_by_offset(
            drag_element, random.randint(0, max_x), random.randint(0, max_y))
        before_posicion = self.get_px_from_style_left_top(
            self.get_posicion_from_style(drag_element))
        self.action_drag_and_drop_by_offset(
            drag_element, random.randint(0, max_x), random.randint(0, max_y))
        after_posicion = self.get_px_from_style_left_top(
            self.get_posicion_from_style(drag_element))
        return before_posicion, after_posicion

    def check_simple_drag(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag = self.element_is_visible(self.locators.SIMPLE_DRAGBOX)
        before_posicion, after_posicion = self.get_before_and_after_posicion(drag)
        return before_posicion, after_posicion

    def check_asix_drag(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        drag_x = self.element_is_visible(self.locators.AXIS_DRAG_ONLY_X)
        drag_y = self.element_is_visible(self.locators.AXIS_DRAG_ONLY_Y)
        before_posicion_x, after_posicion_x = self.get_before_and_after_posicion(drag_x)
        before_posicion_y, after_posicion_y = self.get_before_and_after_posicion(drag_y)
        return after_posicion_x, after_posicion_y

    def check_container_drag(self):
        self.element_is_visible(self.locators.CONTAINER_TAB).click()
        drag_box = self.element_is_visible(self.locators.CONTAINER_DRAG_IN_BOX)
        drag_parent = self.element_is_visible(self.locators.CONTAINER_DRAG_IN_PARENT)
        before_posicion_box, after_posicion_box = self.get_before_and_after_posicion(
            drag_box,max_x = 200)
        before_posicion_parent, after_posicion_parent = self.get_before_and_after_posicion(
            drag_parent)
        return after_posicion_box, after_posicion_parent


    def get_px_from_style_left_top(self, value_of_size):
        left = value_of_size.split(';')[1].split(':')[1].replace(' ', '').replace('px','')
        top = value_of_size.split(';')[2].split(
            ':')[1].replace(' ', '').replace('px', '')
        return left, top
