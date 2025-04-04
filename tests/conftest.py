import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1280,720')
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
