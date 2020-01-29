import os
import pytest

from src import config
from selenium import webdriver

chrome_path = os.path.dirname(os.path.abspath('conftest.py')) + '/ops/chromedriver'


def pytest_addoption(parser):
    parser.addoption(
        '-E', '--env', action='store', default='stage', help='Choose environment: test or prod'
    )


def check_environment(request):
    """
    This method check - what environment should be used in testing session
    """
    option_value = request.config.getoption('--env')

    if option_value == 'stage':
        base_url = f'https://{config.stage_credentials["user_name"]}:{config.stage_credentials["password"]}@jijiit.com'
    else:
        base_url = config.stage_base_page

    return base_url


@pytest.fixture(scope='session')
def browser(request):
    """
    The main fixtures tha yields driver instance to all tests
    """

    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.maximize_window()

    url = check_environment(request)
    driver.get(url)

    yield driver
    driver.quit()
