from src.pages.Base import Base

from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '.qa-fw-field-container:nth-child(5) input')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '.qa-fw-field-container:nth-child(6) input')
    PHONE_FIELD = (By.CSS_SELECTOR, '.qa-fw-field-container:nth-child(7) input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.qa-fw-button')


class RegistrationPage(Base):
    """
    This class contains methods for working with functions that present
    on registration page
    """

    def file_registration_form(self, **kwargs):
        self.send_keys(RegistrationPageLocators.EMAIL_FIELD, kwargs.get('email'))
        self.send_keys(RegistrationPageLocators.PASSWORD_FIELD, kwargs.get('password'))
        self.send_keys(RegistrationPageLocators.FIRST_NAME_FIELD, kwargs.get('first_name'))
        self.send_keys(RegistrationPageLocators.LAST_NAME_FIELD, kwargs.get('last_name'))
        self.send_keys(RegistrationPageLocators.PHONE_FIELD, kwargs.get('phone'))

    def submit_registration_form(self):
        self.click(RegistrationPageLocators.SUBMIT_BUTTON)

    def user_registration(self, **kwargs):
        self.file_registration_form(**kwargs)
        self.submit_registration_form()
