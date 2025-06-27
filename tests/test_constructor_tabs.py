from locators import Locators
from data import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_tabs(driver):
    driver.get(BASE_URL)

    # Переход к "Соусы"
    driver.find_element(*Locators.tab_sauces).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_sauces))
    assert driver.find_element(*Locators.active_tab_sauces)

    # Переход к "Начинки"
    driver.find_element(*Locators.tab_fillings).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_fillings))
    assert driver.find_element(*Locators.active_tab_fillings)

    # Переход обратно к "Булки"
    driver.find_element(*Locators.tab_buns).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.active_tab_buns))
    assert driver.find_element(*Locators.active_tab_buns)
