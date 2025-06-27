import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, USER_EMAIL, USER_PASSWORD
from locators import Locators

class TestLogin:

    def login_flow(self, driver):
        driver.find_element(*Locators.field_email_login).send_keys(USER_EMAIL)
        driver.find_element(*Locators.field_password_login).send_keys(USER_PASSWORD)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.button_login_main).click()
        self.login_flow(driver)

    def test_login_from_register_form(self, driver):
        driver.get(BASE_URL + "/register")
        driver.find_element(*Locators.button_go_to_login_from_register).click()
        self.login_flow(driver)

    def test_login_from_forgot_password_form(self, driver):
        driver.get(BASE_URL + "/forgot-password")
        driver.find_element(*Locators.button_go_to_login_from_forgot_password).click()
        self.login_flow(driver)
