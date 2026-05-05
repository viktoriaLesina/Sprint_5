from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    MAIN_PAGE_URL,
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    CREATE_ACCOUNT_BUTTON,
    USER_AVATAR,
    USER_NAME,
    PASSWORD_INPUT_FIELD,
    PASSWORD_SUBMIT_INPUT_FIELD,
    EMAIL_INPUT_FIELD
)
class TestNewUserRegistration:
    def test_registration(self, driver:WebDriver, user_registration):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(user_registration["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(user_registration["password"])
        driver.find_element(*PASSWORD_SUBMIT_INPUT_FIELD).send_keys(user_registration["password_submit"])
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(USER_AVATAR))
        user_name = wait.until(expected_conditions.visibility_of_element_located(USER_NAME))

        assert user_name.text == "User."
