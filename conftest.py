import pytest
from selenium import webdriver
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo is not None:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            # Take screenshot
            driver = item.funcargs['driver']
            screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
            driver.save_screenshot(screenshot_file)