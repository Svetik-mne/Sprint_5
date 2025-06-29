import pytest
from helpers import login
from locators import Locators
from urls import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL

class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.button_login_main).click()
        login(driver)

    def test_login_from_register_form(self, driver):
        driver.get(REGISTER_URL)
        driver.find_element(*Locators.button_go_to_login_from_register).click()
        login(driver)

    def test_login_from_forgot_password_form(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        driver.find_element(*Locators.button_go_to_login_from_forgot_password).click()
        login(driver)
