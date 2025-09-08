import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_demoqa_title(driver, browser):
    driver.get("https://demoqa.com")
    if browser == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities
    )

    driver.get("https://demoqa.com")
    assert "DEMOQA" in driver.title.upper()

    driver.quit()
