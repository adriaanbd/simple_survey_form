from selenium.webdriver.common.by import By


class SurveyPageLocators(object):
    """A class for main page locators. All locators should come here"""
    HEADER = (By.CSS_SELECTOR, "h1[id='title']")
    SURVEY_FORM = (By.ID, "survey-form")
    NAME_INPUT = (By.ID, "name")
    NAME_LABEL = (By.CSS_SELECTOR, "label[for='name']")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email']")
    AGE_INPUT = (By.ID, "number")
    AGE_LABEL = (By.CSS_SELECTOR, "label[id='number-label']")
    DESCRIPTION = (By.CSS_SELECTOR, "p[id='description']")
    SELECT_DROPDOWN = (By.CSS_SELECTOR, "select[id='dropdown']")
    RADIO_OPTIONS = (By.CSS_SELECTOR, "input[type='radio']")
    CHECKBOX_INPUT = (By.CSS_SELECTOR, "input[type='checkbox']")
    TEXT_AREA = (By.TAG_NAME, "textarea")
    SUBMIT_BUTTON = (By.ID, "submit")
