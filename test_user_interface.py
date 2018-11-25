import os
import unittest
from selenium import webdriver
import page


class SurveyFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(valid_selenium_file_path("survey.html"))

    def test_validate_main_html_components(self):
        survey_page = page.SurveyPage(self.driver)
        self.assertTrue(survey_page.is_title_matches("Survey"))
        self.assertTrue(survey_page.description_id_exists())
        self.assertTrue(survey_page.h1_title_id_exists())
        self.assertTrue(survey_page.survey_form_id_exists())
        self.assertTrue(survey_page.name_input_and_label_coupling_exists())
        self.assertTrue(survey_page.name_input_is_required_attribute())
        self.assertTrue(survey_page.email_input_and_label_coupling_exists())
        self.assertTrue(survey_page.email_input_is_required_attribute())
        self.assertTrue(survey_page.age_input_and_label_coupling_exists())
        self.assertTrue(survey_page.select_tag_with_dropdown_id_exists())
        self.assertTrue(survey_page.radio_input_with_name_attribute_exists())
        self.assertTrue(survey_page.checkbox_input_type_exists())
        self.assertTrue(survey_page.checkboxes_with_value_attribute_exist())
        self.assertTrue(survey_page.textarea_tag_exists())
        self.assertTrue(survey_page.button_tag_with_submit_id_exists())

    def test_form_with_required_inputs_expect_no_errors(self):
        survey_page = page.SurveyPage(self.driver)

        name, email = "John Doe", "example@email.com"

        survey_page.insert_name(name)
        survey_page.insert_email(email)

        self.assertEqual(name, survey_page.get_inserted_name())
        self.assertEqual(email, survey_page.get_inserted_email())

        survey_page.click_submit_button()

        self.assertTrue(survey_page.is_name_html_validation_error())
        self.assertTrue(survey_page.is_email_html_validation_error())

    def test_form_with_all_other_inputs_expect_no_error(self):
        survey_page = page.SurveyPage(self.driver)

        name, email, age = "John Doe", "example@email.com", "18"
        survey_page.insert_name(name)
        survey_page.insert_email(email)
        survey_page.insert_age(age)

        self.assertTrue(survey_page.can_select_random_input_radio_options())
        self.assertTrue(survey_page.can_select_random_dropdown_option())
        self.assertTrue(survey_page.can_select_random_checkbox_options())
        self.assertTrue(survey_page.can_insert_text_into_text_area())

        survey_page.click_submit_button()

    def test_name_validation_error(self):
        survey_page = page.SurveyPage(self.driver)

        name, email = "", "example@email.com"
        survey_page.insert_name(name)
        survey_page.insert_email(email)

        survey_page.click_submit_button()

        self.assertTrue(survey_page.is_name_html_validation_error())

    def test_email_validation_error(self):
        survey_page = page.SurveyPage(self.driver)

        name, email = "John Doe", ""
        survey_page.insert_name(name)
        survey_page.insert_email(email)

        survey_page.click_submit_button()

        self.assertTrue(survey_page.is_email_html_validation_error())

    def test_age_out_of_range_validation_error(self):
        survey_page = page.SurveyPage(self.driver)

        name, email, age = "John Doe", "example@email.com", "0"
        survey_page.insert_name(name)
        survey_page.insert_email(email)
        survey_page.insert_age(age)

        survey_page.click_submit_button()

        self.assertTrue(survey_page.is_age_html_validation_error())

    def test_age_with_non_numbers_expect_error(self):
        survey_page = page.SurveyPage(self.driver)

        name, email, age = "John Doe", "example@email.com", "A"
        survey_page.insert_name(name)
        survey_page.insert_email(email)
        survey_page.insert_age(age)

        survey_page.click_submit_button()

        self.assertTrue(survey_page.is_age_html_validation_error())

    def tearDown(self):
        self.driver.close()


def valid_selenium_file_path(file_name):
    html_file_path = os.getcwd() + "/" + file_name
    valid_file_path = "file:///" + html_file_path
    return valid_file_path


if __name__ == "__main__":
    unittest.main()
