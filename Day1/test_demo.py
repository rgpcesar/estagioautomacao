# test_home_page.py
import time
from selenium import webdriver

def test_verify_demoqa_title():
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com")
    driver.maximize_window()

    assert "DEMOQA" in driver.title
    
    driver.quit()