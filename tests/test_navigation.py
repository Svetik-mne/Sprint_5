import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import login

class TestNavigation:

    def test_personal_area_transition(self, driver):
        login(driver)
        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
        assert driver.find_element(*Locators.button_exit_personal_area).is_displayed()

    def test_constructor_via_header_and_logo(self, driver):
        login(driver)
        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))


        driver.find_element(*Locators.link_constructor).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.tab_buns))
        assert driver.find_element(*Locators.tab_buns)

        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.tab_buns))
        assert driver.find_element(*Locators.tab_buns)
