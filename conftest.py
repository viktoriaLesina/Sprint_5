import pytest
import time
from selenium import webdriver

@pytest.fixture
def user_credentials():
    return{
        "email" : "qwerty1@gmail.com",
        "password" : "qaz",
        "password_submit" : "qaz"
    }

@pytest.fixture
def user_registration():
    return {
    "email" : f"user_{int(time.time())}@mail.com",
    "password" : "qaz",
    "password_submit" : "qaz"
    }

@pytest.fixture
def create_ad():
    return{
        "name" : "some item",
        "description" : "some description",
        "price" : "123"
    }

@pytest.fixture
def invalid_user():
    return {
        "email" : "ladyligeiatop@gmail,com"
    }

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()