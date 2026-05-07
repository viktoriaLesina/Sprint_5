from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    CREATE_ADD,
    CREATE_ADD_POPUP_USER_NOT_AUTHORIZED,
    POPUP_TITLE_USER_NOT_AUTHORIZED,
)

from config import MAIN_PAGE_URL


class TestAddCreationByUbathorizedUser:

    def test_create_add_unathorized(self, driver):
        driver.get(MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        driver.find_element(*CREATE_ADD).click()

        assert wait.until(
            EC.visibility_of_element_located(CREATE_ADD_POPUP_USER_NOT_AUTHORIZED)
        )
        assert wait.until(
            EC.visibility_of_element_located(POPUP_TITLE_USER_NOT_AUTHORIZED)
        )
