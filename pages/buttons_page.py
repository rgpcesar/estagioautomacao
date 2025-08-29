from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ButtonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://demoqa.com/buttons"
        # Locators
        self.DOUBLE_CLICK_BTN = (By.ID, "doubleClickBtn")
        self.RIGHT_CLICK_BTN = (By.ID, "rightClickBtn")
        self.DYNAMIC_CLICK_BTN = (By.XPATH, "//button[text()='Click Me']")
        self.DOUBLE_CLICK_MSG = (By.ID, "doubleClickMessage")
        self.RIGHT_CLICK_MSG = (By.ID, "rightClickMessage")
        self.DYNAMIC_CLICK_MSG = (By.ID, "dynamicClickMessage")
        
    def navigate(self):
        self.driver.get(self.url)

    def perform_double_click(self):
        btn = self.driver.find_element(*self.DOUBLE_CLICK_BTN)
        ActionChains(self.driver).double_click(btn).perform()
        return self.wait.until(EC.visibility_of_element_located(self.DOUBLE_CLICK_MSG)).text

    def perform_right_click(self):
        btn = self.driver.find_element(*self.RIGHT_CLICK_BTN)
        ActionChains(self.driver).context_click(btn).perform()
        return self.wait.until(EC.visibility_of_element_located(self.RIGHT_CLICK_MSG)).text

    def perform_dynamic_click(self):
        btn = self.driver.find_element(*self.DYNAMIC_CLICK_BTN)
        btn.click()
        return self.wait.until(EC.visibility_of_element_located(self.DYNAMIC_CLICK_MSG)).text