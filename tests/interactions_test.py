import pytest

from ..pages.interactions_page import SortablePage


# @pytest.mark.skip
class TestInteractions:

    # @pytest.mark.skip
    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(
                driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"
