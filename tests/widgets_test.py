import pytest

from ..pages.widgets_page import AccordianPage, AutoComplitePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage, ToolTipsPage


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

    @pytest.mark.skip
    class TestDatePicker:

        def test_chenge_date(self, driver):
            date_page = DatePickerPage(
                driver, 'https://demoqa.com/date-picker')
            date_page.open()
            default_date, result = date_page.select_date()
            assert default_date != result, "The date has not been changed"

        def test_chenge_date_and_time(self, driver):
            date_page = DatePickerPage(
                driver, 'https://demoqa.com/date-picker')
            date_page.open()
            default_date, result = date_page.select_date_and_time()
            assert default_date != result, "The date and time has not been changed"

    @pytest.mark.skip
    class TestSlider:

        def test_chenge_slider(self, driver):
            slider_page = SliderPage(
                driver, 'https://demoqa.com/slider')
            slider_page.open()
            default_value, result = slider_page.check_slider()
            assert default_value != result, "The slider has not been changed"

    @pytest.mark.skip
    class TestProgressBar:
        def test_chenge_progress(self, driver):
            progress_page = ProgressBarPage(
                driver, 'https://demoqa.com/progress-bar')
            progress_page.open()
            result = progress_page.check_progress()
            assert result > 0, "The progress has not been changed"

    @pytest.mark.skip
    class TestTabs:

        def test_tabs(self, driver):
            tabs_page = TabsPage(
                driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tabs_list = ['What', 'Origin', 'Use']
            for tab in tabs_list:
                tabs_title, tabs_text = tabs_page.check_tabs(tab)                
                assert tab == tabs_title and len(
                    tabs_text) > 0, f"Tab {tab} does not work"

        @pytest.mark.xfail
        def test_fail_tab_more(self, driver):
            tabs_page = TabsPage(
                driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tabs_title, tabs_text = tabs_page.check_tabs('More')
            assert tabs_title == 'More' and len(
                tabs_text) > 0, "Tab More does not work"

    @pytest.mark.skip
    class TestToolTips:

        def test_tabs(self, driver):
            tool_tips_page = ToolTipsPage(
                driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button,field, contrary, section = tool_tips_page.check_tool_tips()
            assert button == 'You hovered over the Button', "Hover missing or incorrect content"
            assert field == 'You hovered over the text field', "Hover missing or incorrect content"
            assert contrary == 'You hovered over the Contrary', "Hover missing or incorrect content"
            assert section == 'You hovered over the 1.10.32', "Hover missing or incorrect content"

