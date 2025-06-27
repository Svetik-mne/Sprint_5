from locators import Locators
from data import BASE_URL, USER_EMAIL, USER_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(driver):
    driver.get(BASE_URL + "/login")
    driver.find_element(*Locators.field_email_login).send_keys(USER_EMAIL)
    driver.find_element(*Locators.field_password_login).send_keys(USER_PASSWORD)
    driver.find_element(*Locators.button_login).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))

    driver.find_element(*Locators.link_personal_area).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
    driver.find_element(*Locators.button_exit_personal_area).click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_login))
    assert driver.find_element(*Locators.button_login).is_displayed()
