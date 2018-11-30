from selenium.webdriver.common.by import By


class SurveyPageLocators(object):
    """A class for main page locators. All locators should come here"""
    HEADER = (By.CSS_SELECTOR, "h1[id='title']")
    DESCRIPTION = (By.CSS_SELECTOR, "p[id='description']")
    FLASH = (By.ID, "flash-message")
    SURVEY_FORM = (By.ID, "survey-form")
    NAME_INPUT = (By.ID, "name")
    NAME_LABEL = (By.CSS_SELECTOR, "label[for='name']")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email']")
    AGE_INPUT = (By.ID, "age")
    AGE_LABEL = (By.CSS_SELECTOR, "label[for='age']")
    RADIO_OPTIONS = (By.CSS_SELECTOR, "input[type='radio']")
    SELECT_DROPDOWN = (By.CSS_SELECTOR, "select[id='path']")
    CHECKBOX_INPUT = (By.CSS_SELECTOR, "input[type='checkbox']")
    TEXT_AREA = (By.TAG_NAME, "textarea")
    SUBMIT_BUTTON = (By.ID, "submit")
