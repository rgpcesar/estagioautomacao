from selenium.webdriver.common.by import By
import time

def test_fill_text_box_form_and_validate(driver):
    driver.get("https://demoqa.com/text-box")

    # Fill out the form
    full_name_input = driver.find_element(By.ID, "userName")
    submit_button = driver.find_element(By.ID, "submit")

    nome = "Rodrigo"

    full_name_input.send_keys(nome)
    time.sleep(2)
    
    full_name_input.clear()
    time.sleep(2)
    nome = "Prado"

    full_name_input.send_keys(nome)
    time.sleep(3)

    # Click on submit button
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(2)
    
    submit_button.click()
    
    time.sleep(2)
    output_name = driver.find_element(By.ID, "name")
    assert nome in output_name.text
