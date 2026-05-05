from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    CREATE_ADD,
    CREATE_ADD_POPUP_USER_NOT_AUTHORIZED,
    POPUP_TITLE_USER_NOT_AUTHORIZED,
    MAIN_PAGE_URL
)
class TestAddCreationByUbathorizedUser:

    def test_create_add_unathorized(self, driver:WebDriver):
        driver.get(MAIN_PAGE_URL)
        wait = WebDriverWait(driver, 15)
        driver.find_element(*CREATE_ADD).click()
        wait.until(
            expected_conditions.visibility_of_element_located(CREATE_ADD_POPUP_USER_NOT_AUTHORIZED)
        )
        popup_title = driver.find_element(*POPUP_TITLE_USER_NOT_AUTHORIZED)
        assert popup_title.text == "Чтобы разместить объявление, авторизуйтесь"