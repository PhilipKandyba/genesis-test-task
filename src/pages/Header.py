from src.pages.Base import Base

from selenium.webdriver.common.by import By


class UnregisterUserHeaderLocators:
    AUTHORIZATION_LINK = (By.CSS_SELECTOR, '.b-app-header__user-bar span:nth-child(1) a')
    REGISTRATION_LINK = (By.CSS_SELECTOR, '.b-app-header__user-bar span:nth-child(2) a')


class UnregisterUserHeader(Base):
    """
    This header is available only for un-registered user.
    This class implements main methods for interacting with header
    """
    def click_on_authorization_link(self):
        self.click(UnregisterUserHeaderLocators.AUTHORIZATION_LINK)

    def click_on_registration_link(self):
        self.click(UnregisterUserHeaderLocators.REGISTRATION_LINK)


class RegisteredUserHeaderLocators:
    USER_AVATAR_MENU_OPENER = (By.CSS_SELECTOR, '.qa-fw-menu button')
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, '.qa-fw-menu-content-container li:last-child')


class RegisteredUserHeader(Base):
    """
    Class that contains methods for managing functions in this header.
    This header available only registered user after authorization
    """

    def user_logout(self):
        self.hover(RegisteredUserHeaderLocators.USER_AVATAR_MENU_OPENER)
        self.click(RegisteredUserHeaderLocators.SIGN_OUT_BUTTON)