from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    USER_AVATAR,
    USER_NAME,
    LOGOUT_BUTTON,
    LOGIN_AND_REGISTRATION_BUTTON,
)
from config import MAIN_PAGE_URL
from test_data import USER_CREDENTIALS


class TestLogout:
    def test_logout(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(
            USER_CREDENTIALS["password"]
        )
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(USER_AVATAR))
        wait.until(expected_conditions.visibility_of_element_located(USER_NAME))

        driver.find_element(*LOGOUT_BUTTON).click()

        wait.until(
            expected_conditions.visibility_of_element_located(
                LOGIN_AND_REGISTRATION_BUTTON
            )
        )

        assert len(driver.find_elements(*USER_AVATAR)) == 0
        assert len(driver.find_elements(*USER_NAME)) == 0
