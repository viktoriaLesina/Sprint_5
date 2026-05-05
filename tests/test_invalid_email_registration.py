from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_PAGE_URL,
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_INPUT_FIELD,
    CREATE_ACCOUNT_BUTTON,
    ERROR_TEXT
)


class TestInvalidEmailRegistration:

    def test_registration_invalid_email(self, driver: WebDriver, invalid_user):
        wait = WebDriverWait(driver, 15)

        driver.get(MAIN_PAGE_URL)

        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(invalid_user["email"])

        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error = wait.until(
            EC.visibility_of_element_located(ERROR_TEXT)
        )

        assert "Ошибка" == error.text