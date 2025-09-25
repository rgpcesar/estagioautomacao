from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class ToolTipsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/tool-tips"
        self.button = (By.ID, "toolTipButton")
        self.actions = ActionChains(self.driver)

    def navigate(self):
        self.driver.get(self.url)

    
    def go_to_button(self):
        web_element = self.driver.find_element(*self.button)
        self.actions.move_to_element(web_element).perform()
        self.actions.move_to_element()