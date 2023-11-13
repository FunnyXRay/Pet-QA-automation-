from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"
