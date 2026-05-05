from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_PAGE_URL,
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_INPUT_FIELD,
    CREATE_ACCOUNT_BUTTON,
    ERROR_TEXT,
    PASSWORD_INPUT_FIELD,
    PASSWORD_SUBMIT_INPUT_FIELD
)

class TestExistedUserRegistration:
    
    def test_existed_user_registration(self, driver:WebDriver, user_credentials):
        wait = WebDriverWait(driver, 15)
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(user_credentials["password"])
        driver.find_element(*PASSWORD_SUBMIT_INPUT_FIELD).send_keys(user_credentials["password_submit"])
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        error = wait.until(
            EC.visibility_of_element_located(ERROR_TEXT)
        )

        assert "Ошибка" == error.text

