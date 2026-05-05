from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MAIN_PAGE_URL,
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
    USER_ADD_CREATED_CARD
)

class TestAddCreation:
    def test_add_creation(self, driver: WebDriver, user_credentials, create_ad):
        wait = WebDriverWait(driver, 15)

        driver.get(MAIN_PAGE_URL)

        driver.find_element(*LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys(user_credentials["password"])
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(USER_AVATAR))

        driver.find_element(*CREATE_ADD).click()

        driver.find_element(*ITEM_NAME_INPUT_FIELD).send_keys(create_ad["name"])
        driver.find_element(*ITEM_DESCRIPTION_INPUT_FIELD).send_keys(create_ad["description"])
        driver.find_element(*ITEM_PRICE_INPUT_FIELD).send_keys(str(create_ad["price"]))

        driver.find_element(*ITEM_CITY_ARROW_BUTTON).click()
        wait.until(EC.element_to_be_clickable(ITEM_CITY_ENTITY)).click()

        driver.find_element(*ITEM_CATEGORY_ARROW_BUTTON).click()
        wait.until(EC.element_to_be_clickable(ITEM_CATEGORY_ENTITY)).click()

        driver.find_element(*ITEM_CONDITION_RADDIO_BUTTON_USED).click()
        driver.find_element(*ITEM_PUBLISH_BUTTON).click()

        driver.find_element(*USER_AVATAR).click()

        wait.until(EC.visibility_of_element_located(USER_ADDS_SECTION))

        wait.until(EC.presence_of_all_elements_located(USER_ADD_CREATED_CARD))
        cards = driver.find_elements(*USER_ADD_CREATED_CARD)

        assert any(create_ad["name"] in card.text for card in cards)