import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_select_state_and_city(driver):
    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # --- Seleciona o Estado ---
    state_box = wait.until(EC.element_to_be_clickable((By.ID, "state")))
    driver.execute_script("arguments[0].scrollIntoView(true);", state_box)
    time.sleep(5)
    state_box.click()  # abre o dropdown
    time.sleep(5)
    state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'NCR')]")))
    state_option.click()
    

    # --- Seleciona a Cidade ---
    city_box = wait.until(EC.element_to_be_clickable((By.ID, "city")))
    city_box.click()  # abre o dropdown
    time.sleep(5)

    city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Delhi')]")))
    city_option.click()

    time.sleep(5)
    # Validação simples
    selected_state = driver.find_element(By.CSS_SELECTOR, "#state .css-1uccc91-singleValue").text
    selected_city = driver.find_element(By.CSS_SELECTOR, "#city .css-1uccc91-singleValue").text

    assert selected_state == "NCR"
    assert selected_city == "Delhi"
