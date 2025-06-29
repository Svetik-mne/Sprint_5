import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from generation_ep import EmailPasswordGenerator
from data import USER_EMAIL, USER_PASSWORD
from urls import LOGIN_URL
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    gen = EmailPasswordGenerator()
    email, password = gen.generate()
    return email, password

@pytest.fixture
def login_existing_user(driver):
    driver.get(LOGIN_URL)
    driver.find_element(*Locators.field_email).send_keys(USER_EMAIL)
    driver.find_element(*Locators.field_password).send_keys(USER_PASSWORD)
    driver.find_element(*Locators.button_login).click()
    yield driver
