

import pytest
from pages.elements_page import ElementsPage

@pytest.mark.smoke
def test_navigate_to_elements_page(driver):
    """Navega para a página de elementos."""
    elements_page = ElementsPage(driver)
    elements_page.navigate()

    assert "elements" in elements_page.get_url()

@pytest.mark.smoke
def test_locate_by_id(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()

    assert elements_page.text_box_is_visible()
    assert "Text Box" in elements_page.get_text_menu()

@pytest.mark.smoke
def test_locate_by_css_selector(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    
    assert elements_page.check_box_is_visible()

@pytest.mark.smoke
def test_locate_by_xpath(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()

    assert elements_page.radio_button_is_visible()