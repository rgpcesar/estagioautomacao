from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigate_to_elements_page(driver):
    """Navigates to the elements page."""
    driver.get("https://demoqa.com/elements")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main-header"))
    )
    assert "elements" in driver.current_url

def test_locate_by_id(driver):
    driver.get("https://demoqa.com/elements")
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "item-0"))
    )
    assert element.is_displayed()
    assert element.text == "Text Box"

def test_locate_by_css_selector(driver):
    driver.get("https://demoqa.com/elements")
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#item-0"))
    )
    assert element.is_displayed()

def test_locate_by_xpath(driver):
    driver.get("https://demoqa.com/elements")
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Text Box']"))
    )
    assert element.is_displayed()