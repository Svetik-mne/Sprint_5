import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import BASE_URL, REGISTER_URL
from helpers import wait_for_url_contains

class TestRegistration:

    def test_successful_registration(self, driver, new_user):
        email, password = new_user
        driver.get(BASE_URL)
        driver.find_element(*Locators.button_login_main).click()
        driver.find_element(*Locators.button_go_to_register).click()

        driver.find_element(*Locators.field_name).send_keys("Test")
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_register).click()

        wait_for_url_contains(driver, BASE_URL)
        assert BASE_URL in driver.current_url

    def test_invalid_password(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*Locators.field_name).send_keys("Test")
        driver.find_element(*Locators.field_email).send_keys("test@email.ru")
        driver.find_element(*Locators.field_password).send_keys("123")
        driver.find_element(*Locators.button_register).click()

        assert driver.find_element(*Locators.error_password).is_displayed()
