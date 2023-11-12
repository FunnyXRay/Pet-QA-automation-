from pages.elements_page import TextBoxPage
import time
from conftest import driver


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            test_text_box = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_text_box.open()
            full_name, email, current_address, permanent_address = test_text_box.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = test_text_box.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current_address does not match"
            assert permanent_address == output_per_addr, "the permanent_address does not match"
