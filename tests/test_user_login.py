from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    USER_AVATAR,
    USER_NAME,
)
from config import MAIN_PAGE_URL
from test_data import USER_CREDENTIALS


class TestLogin:

    def test_login(self, driver):

        wait = WebDriverWait(driver, 15)

        driver.get(MAIN_PAGE_URL)

        wait.until(EC.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT_FIELD))

        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(
            USER_CREDENTIALS["password"]
        )
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))

        assert user_name.is_displayed()
