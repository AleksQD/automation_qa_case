import pytest
from ..pages.form_page import FormPage


@pytest.mark.skip
class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(
                driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [person.firstname + " " + person.lastname,
                    person.email] == [result[0], result[1]], "The form has not been filled"
