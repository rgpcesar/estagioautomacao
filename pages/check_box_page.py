from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"
        self.wait = WebDriverWait(driver, 10)

        # Locators:
        self.EXPAND_ALL_BTN = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.NOTES_CHECK_BOX = (By.XPATH, "//label[@for='tree-node-notes']")
        self.CHECK_BOX_SELECTED = (By.ID, "tree-node-notes")
    
    def navigate(self):
        self.driver.get(self.url)

    def perform_expand_all_click(self):
        expand_all_button = self.wait.until(EC.element_to_be_clickable(self.EXPAND_ALL_BTN))
        expand_all_button.click()

    def select_notes_checkbox(self):
        notes_checkbox = self.wait.until(EC.element_to_be_clickable(self.NOTES_CHECK_BOX))
        notes_checkbox.click()

    def validate_checkbox_selected(self):
        checkbox_ticked = self.driver.find_element(*self.CHECK_BOX_SELECTED)
        return checkbox_ticked.is_selected()
