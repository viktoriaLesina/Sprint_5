from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_INPUT_FIELD,
    CREATE_ACCOUNT_BUTTON,
    ERROR_TEXT,
)
from config import MAIN_PAGE_URL
from test_data import INVALID_USER


class TestInvalidEmailRegistration:

    def test_registration_invalid_email(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT_FIELD)).send_keys(INVALID_USER["email"])
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_TEXT))
        assert error.is_displayed()
