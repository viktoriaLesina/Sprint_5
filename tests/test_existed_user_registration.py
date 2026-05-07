from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_INPUT_FIELD,
    CREATE_ACCOUNT_BUTTON,
    ERROR_TEXT,
    PASSWORD_INPUT_FIELD,
    PASSWORD_SUBMIT_INPUT_FIELD,
)
from config import MAIN_PAGE_URL
from test_data import USER_CREDENTIALS


class TestExistedUserRegistration:

    def test_existed_user_registration(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.get(MAIN_PAGE_URL)

        wait.until(
            EC.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT_FIELD))
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(
            USER_CREDENTIALS["password"]
        )
        driver.find_element(*PASSWORD_SUBMIT_INPUT_FIELD).send_keys(
            USER_CREDENTIALS["password_submit"]
        )

        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_TEXT))
        assert error.is_displayed()
