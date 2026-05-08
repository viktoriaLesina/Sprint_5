from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    CREATE_ADD,
    ITEM_NAME_INPUT_FIELD,
    ITEM_CITY_ARROW_BUTTON,
    ITEM_CATEGORY_ARROW_BUTTON,
    ITEM_CONDITION_RADDIO_BUTTON_USED,
    ITEM_DESCRIPTION_INPUT_FIELD,
    ITEM_PRICE_INPUT_FIELD,
    USER_ADDS_SECTION,
    USER_AVATAR,
    ITEM_CATEGORY_ENTITY,
    ITEM_CITY_ENTITY,
    ITEM_PUBLISH_BUTTON,
    USER_ADD_CREATED_CARD,
)
from config import MAIN_PAGE_URL
from test_data import CREATE_AD_DATA, USER_CREDENTIALS


class TestAddCreation:
    def test_add_creation(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(MAIN_PAGE_URL)
        wait.until(
            EC.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT_FIELD)).send_keys(
            USER_CREDENTIALS["email"]
        )
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(
            USER_CREDENTIALS["password"]
        )
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        wait.until(EC.element_to_be_clickable(CREATE_ADD)).click()
        wait.until(EC.visibility_of_element_located(ITEM_NAME_INPUT_FIELD)).send_keys(
            CREATE_AD_DATA["name"]
        )
        driver.find_element(*ITEM_DESCRIPTION_INPUT_FIELD).send_keys(
            CREATE_AD_DATA["description"]
        )
        driver.find_element(*ITEM_PRICE_INPUT_FIELD).send_keys(
            str(CREATE_AD_DATA["price"])
        )
        wait.until(EC.element_to_be_clickable(ITEM_CITY_ARROW_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(ITEM_CITY_ENTITY)).click()
        wait.until(EC.element_to_be_clickable(ITEM_CATEGORY_ARROW_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(ITEM_CATEGORY_ENTITY)).click()
        driver.find_element(*ITEM_CONDITION_RADDIO_BUTTON_USED).click()
        driver.find_element(*ITEM_PUBLISH_BUTTON).click()
        wait.until(EC.invisibility_of_element_located(ITEM_PUBLISH_BUTTON))
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()
        wait.until(EC.visibility_of_element_located(USER_ADDS_SECTION))
        wait.until(EC.visibility_of_any_elements_located(USER_ADD_CREATED_CARD))
        cards = driver.find_elements(*USER_ADD_CREATED_CARD)
        assert any(CREATE_AD_DATA["name"] in card.text for card in cards)
