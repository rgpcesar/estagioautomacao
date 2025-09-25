import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class PracticeFormPage: # Form page Practice
    """Page Object for the DemoQA Practice Form page.
    Returns:
    - Navigate: method to go to url
    - fill_form: method to fill a form
    - submit: action to submit form
    - check_modal_visible: method to check visibility of modal webelement """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.gender_radio = (By.XPATH, "//label[text()='{}']")
        self.mobile_input = (By.ID, "userNumber")
        self.dob_input = (By.ID, "dateOfBirthInput")
        self.subjects_input = (By.ID, "subjectsInput")
        self.hobbies_checkbox = (By.XPATH, "//label[text()='{}']")
        self.picture_upload = (By.ID, "uploadPicture")
        self.address_textarea = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")
        self.submit_button = (By.ID, "submit")
        self.out_put_modal = (By.ID, "example-modal-sizes-title-lg")

    @allure.step("Navigate to Practice Form page")
    def navigate(self):
        self.driver.get(self.url)

    @allure.step("Fill the practice form with data")
    def fill_form(self, data):
        with allure.step(f"Fill first name: {data['first_name']}"):
            self.driver.find_element(*self.first_name_input).send_keys(data["first_name"])
        with allure.step(f"Fill last name: {data['last_name']}"):
            self.driver.find_element(*self.last_name_input).send_keys(data["last_name"])
        with allure.step(f"Fill email: {data['email']}"):
            self.driver.find_element(*self.email_input).send_keys(data["email"])
        with allure.step(f"Select gender: {data['gender']}"):
            self.driver.find_element(By.XPATH, f"//label[text()='{data['gender']}']").click()
        with allure.step(f"Fill mobile number: {data['mobile']}"):
            self.driver.find_element(*self.mobile_input).send_keys(data["mobile"])
        
        with allure.step(f"Select date of birth: {data['dob']}"):
            dob_field = self.driver.find_element(*self.dob_input)
            dob_field.send_keys(Keys.CONTROL + "a")
            dob_field.send_keys(data["dob"])
            dob_field.send_keys(Keys.ENTER)

        with allure.step(f"Select subjects: {data['subjects']}"):
            subjects_field = self.driver.find_element(*self.subjects_input)
            for subject in data["subjects"]:
                subjects_field.send_keys(subject)
                subjects_field.send_keys(Keys.ENTER)

        with allure.step(f"Select hobbies: {data['hobbies']}"):
            for hobby in data["hobbies"]:
                element = self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
                self.driver.execute_script("arguments[0].click();", element)

        with allure.step(f"Fill address: {data['address']}"):
            self.driver.find_element(*self.address_textarea).send_keys(data["address"])
        
        with allure.step(f"Select state and city: {data['state']} - {data['city']}"):
            state_element = self.driver.find_element(*self.state_dropdown)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", state_element)
            state_element.click()
            (By.XPATH, "//div[contains(text(), 'NCR')]")
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{data['state']}')]").click()
            city_element = self.driver.find_element(*self.city_dropdown)
            city_element.click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{data['city']}')]").click()

    @allure.step("Submit the form")
    def submit_form(self):
        button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.find_element(*self.submit_button).click()

    @allure.step("Check if modal is present")
    def check_modal_visible(self):
        return self.driver.find_element(*self.out_put_modal).is_displayed()
