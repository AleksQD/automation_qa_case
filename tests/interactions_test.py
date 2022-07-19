import pytest

from ..pages.interactions_page import DroppablePage, ResizablePage, SelectablePage, SortablePage


# @pytest.mark.skip
class TestInteractions:

    @pytest.mark.skip
    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(
                driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"

    @pytest.mark.skip
    class TestSelectable:
        def test_select(self, driver):
            selectable_page = SelectablePage(
                driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            number_active_list = selectable_page.check_select_list()
            number_active_grid = selectable_page.check_select_grid()
            assert number_active_list > 0, "No active list items"
            assert number_active_grid > 0, "No active grid items"

    @pytest.mark.skip
    class TestResizable:
        def test_resize(self, driver):
            resizable_page = ResizablePage(
                driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size_box, min_size_box = resizable_page.chenge_size_resizable_box()
            max_size, min_size = resizable_page.chenge_size_resizable()
            assert max_size_box == (
                '500px', '300px'), "Maximum size not equal to '500px', '300px'"
            assert min_size_box == (
                '150px', '150px'), "Minimum size not equal to '150px', '150px'"
            assert max_size != min_size_box, "Resizeble has not been changed"

    @pytest.mark.skip
    class TestDroppable:
        def test_droppable(self, driver):
            droppable_page = DroppablePage(
                driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            simple_result = droppable_page.check_simple_drop()
            not_acceptable_result = droppable_page.check_accept_drop(
                'not_accept')
            acceptable_result = droppable_page.check_accept_drop('accept')
            not_greedy_result = droppable_page.check_prevent_propogation(
                'not_greedy')
            greedy_result = droppable_page.check_prevent_propogation('greedy')
            revert_after_move, revert_result = droppable_page.check_revert('revert')
            not_revert_after_move, not_revert_result = droppable_page.check_revert(
                'not_revert')
            assert simple_result == 'Dropped!', "The element has not been dropped"
            assert not_acceptable_result == 'Drop here', "The dropped element has been accepted"
            assert acceptable_result == 'Dropped!', "The dropped element has not been accepted"
            assert not_greedy_result[0] == not_greedy_result[1], "Not a greedy box mistakenly greedy"
            assert greedy_result[0] != greedy_result[1], "The greedy box is mistakenly not greedy"
            assert revert_result != revert_after_move, "The element has not reverted"
            assert not_revert_result == not_revert_after_move, "The element has reverted"
