
import random
import time
import pytest
from ..pages.elemets_page import CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage


class TestElements:
    @pytest.mark.skip
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, curr_address, perm_address = text_box_page.fill_all_fields()
            out_name, out_email, out_curr_add, out_perm_add = text_box_page.check_filled_form()
            assert full_name == out_name, 'the full name does not match'
            assert email == out_email, 'the email does not match'
            assert curr_address == out_curr_add, 'the current address does not match'
            assert perm_address == out_perm_add, 'the permanent address does not match'

    @pytest.mark.skip
    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(
                driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    @pytest.mark.skip
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(
                driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            click_button = radio_button_page.click_random_radio_button()
            output_result = radio_button_page.get_output_result()
            assert click_button == output_result, 'radio-button have not been selected(maybe: random choose the "NO"button  - it is disabled)'

    class TestWebTable:
        @pytest.mark.skip
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_person()
            assert new_person in table_result, "The person was not added in table"

        @pytest.mark.skip
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(keyword)
            table_result = web_table_page.check_search_person()
            assert keyword in table_result, "The person was not found in table"

        @pytest.mark.skip
        def test_web_table_update_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "The person card has not been change"

        @pytest.mark.skip
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person card has not delete"

        @pytest.mark.skip
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            rows = web_table_page.select_up_to_some_rows()
            assert rows == [
                5, 10, 20, 25, 50, 100], "The number of rows in table has not been changed"
