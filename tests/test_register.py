import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import BASE_URL

class TestRegistration:

    def test_successful_registration(self, driver, new_user):
        email, password = new_user
        driver.get(BASE_URL)
        driver.find_element(*Locators.button_login_main).click()  # Переход к форме входа
        driver.find_element(*Locators.button_go_to_register).click()  # Переход к форме регистрации

        driver.find_element(*Locators.field_name).send_keys("Test")
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)

        driver.find_element(*Locators.button_register).click()

        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL))
        assert BASE_URL in driver.current_url

    def test_invalid_password(self, driver):
        driver.get(BASE_URL + "/register")

        driver.find_element(*Locators.field_name).send_keys("Test")
        driver.find_element(*Locators.field_email).send_keys("test@email.ru")
        driver.find_element(*Locators.field_password).send_keys("123")  # Пароль < 6 символов

        driver.find_element(*Locators.button_register).click()

        # Проверка, что ошибка видна (нужен локатор)
        assert driver.find_element(*Locators.error_password).is_displayed()
