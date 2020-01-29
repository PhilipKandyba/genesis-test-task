from selenium.common.exceptions import TimeoutException

from src.pages.Base import Base

from selenium.webdriver.common.by import By


class UserDashboardPageLocators:
    PROFILE_DASHBOARD_AVATAR = (By.CSS_SELECTOR, '.b-user-settings__avatarblock')
    PROFILE_DASHBOARD_AVATAR_V2 = (By.CSS_SELECTOR, '.b-profile-sidebar__header__avatar')


class UserDashboardPage(Base):
    """
    Class is describing functionality that available on user dashboard
    The page is available after user authorization
    """
    def is_dashboard_present(self):

        # Hook!
        # Sometimes after authorization we got another "profile" page
        # It have another design and elements
        # Also, page dont have ".http" in url
        # And we need to check two different ways
        # If we have element with one design we chen one element or we check another but the same element
        # TODO: Get answer, why after the same actions (authorization) we can have two different 'account' pages

        try:
            return self.is_element_present(UserDashboardPageLocators.PROFILE_DASHBOARD_AVATAR)
        except TimeoutException:
            return self.is_element_present(UserDashboardPageLocators.PROFILE_DASHBOARD_AVATAR_V2)
