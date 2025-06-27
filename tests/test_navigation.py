from locators import Locators
from data import BASE_URL, USER_EMAIL, USER_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigation:

    def login(self, driver):
        driver.get(BASE_URL + "/login")
        driver.find_element(*Locators.field_email_login).send_keys(USER_EMAIL)
        driver.find_element(*Locators.field_password_login).send_keys(USER_PASSWORD)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))

    def test_personal_area_transition(self, driver):
        self.login(driver)
        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
        assert driver.find_element(*Locators.button_exit_personal_area).is_displayed()

    def test_constructor_from_personal_area(self, driver):
        self.login(driver)
        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))

        # По ссылке "Конструктор"
        driver.find_element(*Locators.link_constructor).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.tab_buns))
        assert driver.find_element(*Locators.tab_buns)

        # По клику на логотип
        driver.find_element(*Locators.link_personal_area).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.button_exit_personal_area))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.tab_buns))
        assert driver.find_element(*Locators.tab_buns)
