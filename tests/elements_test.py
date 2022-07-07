

import random
import time
import pytest
from ..pages.elemets_page import ButtonsPage, CheckBoxPage, DynamicPropertiesPage, LinksPage, RadioButtonPage, TextBoxPage, UploadDownloadPage, WebTablePage


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
            assert curr_address == out_curr_add, "The current address does not match"
            assert perm_address == out_perm_add, "The permanent address does not match"

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
            assert input_checkbox == output_result, "Checkboxes have not been selected"

    @pytest.mark.skip
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(
                driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            click_button = radio_button_page.click_random_radio_button()
            output_result = radio_button_page.get_output_result()
            assert click_button == output_result, "Radio-button have not been selected(maybe: random choose the NO_button  - it is disabled)"

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

    @pytest.mark.skip
    class TestButtonsPage:
        def test_different_click_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.double_click_on_button()
            right = buttons_page.right_click_on_button()
            one = buttons_page.one_click_on_button()
            assert double == "You have done a double click", "The double_click_me  button was not pressed"
            assert right == "You have done a right click", "The right_click_me button was not pressed"
            assert one == "You have done a dynamic click", "The click_me button was not pressed"

    class TestLinksPage:
        @pytest.mark.skip
        def test_check_new_tab_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @pytest.mark.skip
        def test_status_code(self, driver):
            links = {'created': 201, 'no-content': 204, 'moved': 301,
                     'bad-request': 400, 'unauthorized': 401,
                     'forbidden': 403, 'invalid-url': 404}
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            for key, value in links.items():
                response_code = links_page.check_status_code_link(
                    f'https://demoqa.com/{key}')
                assert response_code == value, "Status code wrong"

    class TestUploadDownloadPage:
        @pytest.mark.skip
        def test_check_upload_file(self, driver):
            upload_page = UploadDownloadPage(
                driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "The file has not been uploaded"

        @pytest.mark.skip
        def test_check_dounload_file(self, driver):
            dounload_page = UploadDownloadPage(
                driver, 'https://demoqa.com/upload-download')
            dounload_page.open()
            check = dounload_page.download_file()
            assert check is True, "The file has not been downloaded"

    class TestDynamicPropertiesPage:

        @pytest.mark.skip
        def test_check_enable_button(self, driver):
            dynamic_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            enable = dynamic_page.check_enable_button()
            assert enable is True, "Button did not enable after 5 second"

        @pytest.mark.skip
        def test_dinamic_properties(self, driver):
            dynamic_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            color_before, color_after = dynamic_page.check_chenged_of_color()
            assert color_before != color_after, "Colors have not been changed"

        @pytest.mark.skip
        def test_appear_button(self, driver):
            dynamic_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_page.open()
            appeard = dynamic_page.check_appear_button()
            assert appeard is True, "Button did not appear after 5 second"
