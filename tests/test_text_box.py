from pages.text_box_page import TextBoxPage
import pytest

@pytest.mark.elements
def test_fill_text_box_form(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.navigate()
    
    # Dados de teste
    full_name = "Rodrigo Prado"
    email = "rgp@cesar.org.br"
    current_address = "Rua Barão de Souza Leão, s/n"
    permanent_address = "Avenida Boa Viagem, s/n"
    
    text_box_page.fill_form(full_name, email, current_address, permanent_address)
    text_box_page.submit()
    
    output = text_box_page.get_output_text()
    
    assert f"Name:{full_name}" in output
    assert f"Email:{email}" in output
    assert f"Current Address :{current_address}" in output
    # assert f"Permanent Address :{permanent_address}" in output
    assert f"Permananet Address :{permanent_address}" in output
