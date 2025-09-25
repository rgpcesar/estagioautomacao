from pages.check_box_page2 import CheckBoxPage
import pytest

@pytest.mark.regression
def test_check_box(driver):
    check_box = CheckBoxPage(driver)
    check_box.navigate()
    
    # Expand the tree    
    check_box.click_expand_all()

    # # Select the checkbox "Notes"
    check_box.click_label_notes()
    
    # # Validate if checkbox was ticked
    # notes_input = driver.find_element(By.ID, "tree-node-notes")
    assert check_box.check_notes_is_selected()
