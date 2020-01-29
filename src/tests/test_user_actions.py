from src.lib import random_data

from src.pages.RegistrationPage import RegistrationPage
from src.pages.AuthorizationPage import AuthorizationPage
from src.pages.UserDashboardPage import UserDashboardPage
from src.pages.Header import RegisteredUserHeader, UnregisterUserHeader


class TestUserActions:

    def test_user_registration(self, browser):
        """
        Test scenario:
        1. User get to index page and click on registration link
        2. Fill and submit registration form
        3. After auto-login he exit from the account
        4. User re-authorize to account with data that he use on registration
        5. Checks: If user dashboard is visible
        """

        user_data_dict = random_data.get_random_user_data()

        registration_page = RegistrationPage(browser)
        profile_dashboard = UserDashboardPage(browser)
        authorization_page = AuthorizationPage(browser)
        registered_header = RegisteredUserHeader(browser)
        unregistered_header = UnregisterUserHeader(browser)

        unregistered_header.click_on_registration_link()

        registration_page.user_registration(**user_data_dict)

        registered_header.user_logout()

        unregistered_header.click_on_authorization_link()

        authorization_page.user_authorization(
            email=user_data_dict.get('email'),
            password=user_data_dict.get('password'),
        )

        assert profile_dashboard.is_dashboard_present() is True
