import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from generation_ep import EmailPasswordGenerator

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
    from locators import Locators
    from data import BASE_URL
    driver.get(BASE_URL + "/login")
    driver.find_element(*Locators.field_email).send_keys("your_email@example.com")
    driver.find_element(*Locators.field_password).send_keys("your_password")
    driver.find_element(*Locators.button_login).click()
    yield driver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # или другой драйвер
    driver.maximize_window()
    yield driver
    driver.quit()