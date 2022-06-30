
import pytest
from ..pages.elemets_page import CheckBoxPage, TextBoxPage


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
