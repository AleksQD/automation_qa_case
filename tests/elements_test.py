
import time
from ..pages.elemets_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, curr_address, perm_address = text_box_page.fill_all_fields()
            out_name, out_email, out_curr_add, out_perm_add = text_box_page.check_filled_form()
            assert full_name == out_name
            assert email == out_email
            assert curr_address == out_curr_add
            assert perm_address == out_perm_add