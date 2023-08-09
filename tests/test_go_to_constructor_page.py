from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestGoToConstructorPage:
    def test_click_to_go_to_constructor(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.TEXT_ON_PAGE_PERSONAL_ACCOUNT))).text
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'

    def test_click_to_go_to_stellar_burgers(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.TEXT_ON_PAGE_PERSONAL_ACCOUNT))).text
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'