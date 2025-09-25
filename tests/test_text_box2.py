from selenium.webdriver.common.by import By
import time
from pages.text_box_page import TextBoxPage

def test_fill_text_box_form_and_validate(driver):
    text_box_page = TextBoxPage(driver)

    text_box_page.navigate()

     # Test data for the form
    full_name = "Rodrigo"
    email = "rgpe@cesar.org.br"
    current_address = "Rua Barão de Souza Leão, s/n"
    permanent_address = "Avenida Boa Viagem, s/n"

    text_box_page.fill_form(full_name, email, current_address, permanent_address)

    text_box_page.submit()

    output = text_box_page.get_output_text()

    assert full_name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output
    