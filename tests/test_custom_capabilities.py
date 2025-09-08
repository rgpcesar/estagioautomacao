import pytest
from selenium import webdriver

def test_custom_platform(request):
    """
    This test demonstrates how to pass custom capabilities to the Selenium Grid.
    It requests a specific platform and browser version.
    """
    browser = request.config.getoption("--browser").lower()
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.platform_name = "linux"
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.platform_name = "linux"
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.platform_name = "linux"
    else:
        pytest.skip(f"Browser '{browser}' not configured for this test.")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    
    try:
        assert "linux" in driver.capabilities['platformName'].lower()
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()
