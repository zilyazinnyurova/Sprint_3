from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestSignInPage:
    def test_sign_in_by_enter_in_account(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_by_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_from_registration(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.LINK_SIGN_IN).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_from_password_recovery_page(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.LINK_RESTORE_PASSWORD_ON_PAGE_LOGIN).click()
        driver.find_element(*Locators.LINK_SIGN_IN).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys("zilya_zinnyurova_12_999@gmail.com")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("jhg35TRFw")
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_MAKE_AN_ORDER))).text
        assert orders_link_text == 'Оформить заказ'

