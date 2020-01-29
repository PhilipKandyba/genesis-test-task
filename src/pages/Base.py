from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Base(object):
    """
    The main that contains drivers methods

    You need to inherit in page classes
    """

    wait_time = 10

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        return self.driver.get(url)

    def click(self, locator, wait=wait_time):
        return WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_element(self, locator, wait=wait_time):
        return WebDriverWait(self.driver, wait).until(
            EC.presence_of_element_located(locator)
        )

    def send_keys(self, locator, data, wait=wait_time):
        WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located(locator)
        ).clear()

        return self.get_element(locator).send_keys(data)

    def hover(self, locator, wait=wait_time):
        WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located(locator)
        )

        return ActionChains(
            self.driver
        ).move_to_element(
            self.get_element(locator)
        ).perform()

    def is_element_present(self, locator, wait=wait_time):
        return WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()
