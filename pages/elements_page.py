from selenium.webdriver.common.by import By

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        self.text_box_id = (By.ID, "item-0")
        self.check_box_css = (By.CSS_SELECTOR, "#item-1")
        self.radio_button_xpath = (By.XPATH, "//span[text()='Radio Button']")

    def navigate(self):
        self.driver.get(self.url)

    def get_url(self):
        return self.driver.current_url
    
    def text_box_is_visible(self):
        return self.driver.find_element(*self.text_box_id).is_displayed()
    
    def check_box_is_visible(self):
        return self.driver.find_element(*self.check_box_css).is_displayed()
    
    def radio_button_is_visible(self):
        return self.driver.find_element(*self.radio_button_xpath).is_displayed()
    
    def get_text_menu(self):
        visible_text = self.driver.find_element(*self.text_box_id).text
        return visible_text