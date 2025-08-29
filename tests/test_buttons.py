from pages.buttons_page import ButtonsPage
import pytest

@pytest.mark.buttons
def test_all_button_clicks(driver):
    buttons_page = ButtonsPage(driver)
    buttons_page.navigate()

    # Double Click
    double_click_msg = buttons_page.perform_double_click()
    assert "You have done a double click" in double_click_msg

    # Right Click
    right_click_msg = buttons_page.perform_right_click()
    assert "You have done a right click" in right_click_msg

    # Dynamic Click
    dynamic_click_msg = buttons_page.perform_dynamic_click()
    assert "You have done a dynamic click" in dynamic_click_msg