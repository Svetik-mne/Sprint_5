import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import LOGIN_URL, BASE_URL

class TestLogout:

    def test_logout(self, driver):
        driver.get(LOGIN_URL)
        driver.find_element(*Locators.field_email_login).send_keys(USER_EMAIL)
        driver.find_element(*Locators.field_password_login).send_keys(USER_PASSWORD)
        driver.find_element(*Locators.button_login).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))

        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
        driver.find_element(*Locators.button_exit_personal_area).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()
