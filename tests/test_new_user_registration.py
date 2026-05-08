from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    NO_ACCOUNT_BUTTON,
    CREATE_ACCOUNT_BUTTON,
    USER_AVATAR,
    USER_NAME,
    PASSWORD_INPUT_FIELD,
    PASSWORD_SUBMIT_INPUT_FIELD,
    EMAIL_INPUT_FIELD,
)
from config import MAIN_PAGE_URL
from helpers import get_user_registration_data


class TestNewUserRegistration:

    def test_registration(self, driver):

        wait = WebDriverWait(driver, 10)

        driver.get(MAIN_PAGE_URL)

        user_registration_data = get_user_registration_data()
        wait.until(EC.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT_FIELD))
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(
            user_registration_data["email"]
        )
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(
            user_registration_data["password"]
        )
        driver.find_element(*PASSWORD_SUBMIT_INPUT_FIELD).send_keys(
            user_registration_data["password_submit"]
        )
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))
        assert user_name.is_displayed()
