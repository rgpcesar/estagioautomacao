import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.check_box_page import CheckBoxPage


def test_check_box(driver):
    checkbox_page = CheckBoxPage(driver)
    checkbox_page.navigate()

    # Expand the tree
    checkbox_page.perform_expand_all_click()

    # Select the checkbox "Notes"
    checkbox_page.select_notes_checkbox()
    
    
    # Validate if checkbox was ticked
    assert checkbox_page.validate_checkbox_selected()