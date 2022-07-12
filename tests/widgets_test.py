import pytest

from ..pages.widgets_page import AccordianPage


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
