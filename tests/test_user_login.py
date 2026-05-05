from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    USER_AVATAR,
    MAIN_PAGE_URL,
    USER_NAME,
)

class TestLogin:
    def test_login(self, driver: WebDriver, user_credentials):
        wait = WebDriverWait(driver, 15)
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(user_credentials["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(USER_AVATAR))
        user_name = wait.until(expected_conditions.visibility_of_element_located(USER_NAME))

        assert user_name.text == "User."
