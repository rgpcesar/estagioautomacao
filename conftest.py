import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup: initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver = webdriver.Firefox()
    yield driver
    # Teardown: close the WebDriver
    driver.quit()