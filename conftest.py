import pytest
from selenium import webdriver
import os
import sys

import pytest_html
# Add the project root to the Python path
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import time

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome, firefox, or edge)")
    parser.addoption("--remote", action="store_true", default=True, help="run tests on selenium grid")

@pytest.fixture
def driver(request):
    """Initializes and returns a Selenium WebDriver instance.

    Supports both local and remote execution on Selenium Grid.
    The browser can be specified via the --browser command-line option.
    Remote execution is enabled with the --remote flag.
    """
    remote = request.config.getoption("--remote")
    browser = request.config.getoption("--browser").lower()
    
    if remote:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser == "edge":
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Browser '{browser}' is not supported for remote execution.")
            
        driver_instance = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
    else:
        if browser == "chrome":
            driver_instance = webdriver.Chrome()
        elif browser == "firefox":
            driver_instance = webdriver.Firefox()
        elif browser == "edge":
            driver_instance = webdriver.Edge()
        else:
            raise ValueError(f"Browser '{browser}' is not supported for local execution.")

    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

from pathlib import Path

LOG_FILE = Path("test_durations.log")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    print(msg)
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)

    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

# opcional: limpar o log no início da sessão
def pytest_sessionstart(session):
    LOG_FILE.write_text("=== Test Durations Log ===\n", encoding="utf-8")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take screenshot
        driver = item.funcargs['driver']
        screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
        driver.save_screenshot(screenshot_file)
        # Add screenshot to the HTML report
        if screenshot_file:
            html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
                   f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
    report.extra = extra
