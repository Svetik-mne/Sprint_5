# tests/test_tabs.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import MAIN_URL

class TestTabs:

    def test_switch_to_sauces(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*Locators.tab_sauces).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_sauces))
        assert driver.find_element(*Locators.active_tab_sauces)

    def test_switch_to_fillings(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*Locators.tab_fillings).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_fillings))
        assert driver.find_element(*Locators.active_tab_fillings)

    def test_switch_to_buns(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*Locators.tab_buns).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_buns))
        assert driver.find_element(*Locators.active_tab_buns)