from src.pages.Base import Base

from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '.qa-fw-field-container:nth-child(3) input')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.qa-fw-field-container:nth-child(4) input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.qa-fw-button')


class AuthorizationPage(Base):

    """
    The class implements methods that user can do on authorization page
    """

    def fill_login_form(self, email, password):
        self.send_keys(AuthorizationPageLocators.EMAIL_FIELD, email)
        self.send_keys(AuthorizationPageLocators.PASSWORD_FIELD, password)

    def submit_registration_form(self):
        self.click(AuthorizationPageLocators.SUBMIT_BUTTON)

    def user_authorization(self, email, password):
        self.fill_login_form(email, password)
        self.submit_registration_form()

