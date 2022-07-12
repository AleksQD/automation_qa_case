import pytest

from ..pages.widgets_page import AccordianPage, AutoComplitePage


# @pytest.mark.skip
class TestWidgets:

    @pytest.mark.skip
    class TestAccordianWidget:
        def test_accordian_widget(self, driver):
            accordian_page = AccordianPage(
                driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian_text(
                'first')
            second_title, second_content = accordian_page.check_accordian_text(
                'second')
            third_title, third_content = accordian_page.check_accordian_text(
                'third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "The accordian does not working"
            assert second_title == 'Where does it come from?' and second_content > 0, "The accordian does not working"
            assert third_title == 'Why do we use it?' and third_content > 0, "The accordian does not working"

    @pytest.mark.skip
    class TestAutoComplite:

        def test_fill_multy_autocomplite(self, driver):
            auto_complite_page = AutoComplitePage(
                driver, 'https://demoqa.com/auto-complete')
            auto_complite_page.open()
            colors = auto_complite_page.fill_autocomplite_multiple_input()
            colors_result = auto_complite_page.check_colors_in_input_multy()
            assert colors == colors_result, "The added colors are missing in the input"

        def test_remove_multy_autocomplite(self, driver):
            auto_complite_page = AutoComplitePage(
                driver, 'https://demoqa.com/auto-complete')
            auto_complite_page.open()
            auto_complite_page.fill_autocomplite_multiple_input()
            count_value, count_result = auto_complite_page.remove_value_from_multy()
            assert count_value > count_result, "Value was not deleted"

        def test_fill_single_autocomplite(self, driver):
            auto_complite_page = AutoComplitePage(
                driver, 'https://demoqa.com/auto-complete')
            auto_complite_page.open()
            color = auto_complite_page.fill_autocomplite_single_input()
            color_result = auto_complite_page.check_color_in_input_single()
            assert color == color_result, "The added color are missing in the input"
