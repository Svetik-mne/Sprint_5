from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import LOGIN_URL, MAIN_URL

def login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(*Locators.field_email_login).send_keys(USER_EMAIL)
    driver.find_element(*Locators.field_password_login).send_keys(USER_PASSWORD)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))


def wait_for_url_to_be(driver, url, timeout=10):
    WebDriverWait(driver, timeout).until(EC.url_to_be(url))

def wait_for_url_contains(driver, text, timeout=10):
    WebDriverWait(driver, timeout).until(EC.url_contains(text))
