from locators import SurveyPageLocators as SurveyLocators
from selenium.webdriver.support.ui import Select
import random


class BasePage(object):
    """Base class to initialize the base page to be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SurveyPage(BasePage):
    """Survey page action methods come here"""

    def is_title_matches(self, title):
        """Verifies that the title text appears in page title"""
        return title in self.driver.title

    def description_id_exists(self):
        if self.driver.find_element(*SurveyLocators.DESCRIPTION):
            return True
        return False

    def survey_form_id_exists(self):
        if self.driver.find_element(*SurveyLocators.SURVEY_FORM):
            return True
        return False

    def h1_title_id_exists(self):
        element = self.driver.find_elements(*SurveyLocators.HEADER)
        if element:
            return True
        return False

    def name_input_and_label_coupling_exists(self):
        input_element = self.driver.find_elements(*SurveyLocators.NAME_INPUT)
        label_element = self.driver.find_elements(*SurveyLocators.NAME_LABEL)
        if input_element and label_element:
            return True
        return False

    def email_input_and_label_coupling_exists(self):
        input_element = self.driver.find_elements(*SurveyLocators.EMAIL_INPUT)
        label_element = self.driver.find_elements(*SurveyLocators.EMAIL_LABEL)
        if input_element and label_element:
            return True
        return False

    def age_input_and_label_coupling_exists(self):
        input_element = self.driver.find_elements(*SurveyLocators.AGE_INPUT)
        label_element = self.driver.find_elements(*SurveyLocators.AGE_LABEL)
        if input_element and label_element:
            return True
        return False

    def radio_input_with_name_attribute_exists(self):
        element = self.driver.find_elements(*SurveyLocators.RADIO_OPTIONS)
        assert len(element) > 1
        return all(item.get_attribute("value") for item in element)

    def select_tag_with_dropdown_id_exists(self):
        element = self.driver.find_elements(*SurveyLocators.SELECT_DROPDOWN)
        if element:
            return True
        return False

    def checkbox_input_type_exists(self):
        element = self.driver.find_elements(*SurveyLocators.CHECKBOX_INPUT)
        if element:
            return True
        return False

    def checkboxes_with_value_attribute_exist(self):
        element = self.driver.find_elements(*SurveyLocators.CHECKBOX_INPUT)
        assert len(element) > 1
        return all(item.get_attribute("value") for item in element)

    def name_input_is_required_attribute(self):
        element = self.driver.find_element(*SurveyLocators.NAME_INPUT)
        return "true" in element.get_attribute("required")

    def email_input_is_required_attribute(self):
        element = self.driver.find_element(*SurveyLocators.EMAIL_INPUT)
        return "true" in element.get_attribute("required")

    def insert_name(self, name):
        element = self.driver.find_element(*SurveyLocators.NAME_INPUT)
        element.send_keys(name)

    def get_inserted_name(self):
        element = self.driver.find_element(*SurveyLocators.NAME_INPUT)
        return element.get_attribute("value")

    def is_name_html_validation_error(self):
        element = self.driver.find_element(*SurveyLocators.NAME_INPUT)
        validation_message = element.get_attribute("validationMessage")
        if validation_message:
            return True
        return False

    def insert_email(self, email):
        element = self.driver.find_element(*SurveyLocators.EMAIL_INPUT)
        element.send_keys(email)

    def get_inserted_email(self):
        element = self.driver.find_element(*SurveyLocators.EMAIL_INPUT)
        return element.get_attribute("value")

    def is_email_html_validation_error(self):
        element = self.driver.find_element(*SurveyLocators.EMAIL_INPUT)
        validation_message = element.get_attribute("validationMessage")
        if validation_message:
            return True
        return False

    def insert_age(self, age):
        element = self.driver.find_element(*SurveyLocators.AGE_INPUT)
        element.send_keys(age)

    def get_inserted_age(self):
        element = self.driver.find_element(*SurveyLocators.AGE_INPUT)
        return element.get_attribute("value")

    def is_age_html_validation_error(self):
        element = self.driver.find_element(*SurveyLocators.AGE_INPUT)
        validation_message = element.get_attribute("validationMessage")
        if validation_message:
            return True
        return False

    def can_select_random_input_radio_options(self):
        element = self.driver.find_elements(*SurveyLocators.RADIO_OPTIONS)
        choice = random.choice(element)
        choice.click()

        return any(item.is_selected() for item in element)

    def can_select_random_dropdown_options(self):
        element = Select(
            self.driver.find_element(*SurveyLocators.SELECT_DROPDOWN))
        options = element.options
        values = [
            item.get_attribute("value")
            for item in options
            if item.get_attribute("value") != ''
        ]
        value = random.choice(values)  # select random value from values
        element.select_by_value(value)

        return value in values

    def can_select_random_checkbox_options(self):
        element = self.driver.find_elements(
            *SurveyLocators.CHECKBOX_INPUT
        )
        random.choice(element).click()
        random.choice(element).click()
        random.choice(element).click()

        return any(item.is_selected() for item in element)

    def textarea_tag_exists(self):
        element = self.driver.find_elements(*SurveyLocators.TEXT_AREA)
        if element:
            return True
        return False

    def can_insert_text_into_text_area(self):
        element = self.driver.find_element(*SurveyLocators.TEXT_AREA)
        text = "Hello, World!"
        element.send_keys(text)

        return text in element.get_attribute("value")

    def button_tag_with_submit_id_exists(self):
        element = self.driver.find_elements(*SurveyLocators.SUBMIT_BUTTON)
        if element:
            return True
        return False

    def click_submit_button(self):
        """Submits the form"""
        element = self.driver.find_element(*SurveyLocators.SUBMIT_BUTTON)
        element.click()

    def does_flash_submission_message_exist(self):
        """Gets the text from "id='flash-message" if any"""
        element = self.driver.find_element(*SurveyLocators.FLASH)
        if element.text:
            return True
        return False
