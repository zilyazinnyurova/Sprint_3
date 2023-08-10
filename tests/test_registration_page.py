import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestRegistrationPage:

     def test_registration(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys("Зиля")
        numbers_rand = random.randint(000, 999)
        email = "zilya_zinnyurova_12_" + str(numbers_rand) + "@gmail.com"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("11%gjcRsx#ilo")
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        title_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Locators.TITLE_LOGIN))).text
        assert title_text == 'Вход'

     def test_registration_password_entry_error(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTER).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys("Зиля")
        numbers_rand = random.randint(000, 999)
        email = "zilya_zinnyurova_12_" + str(numbers_rand) + "@gmail.com"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("11%")
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        text_error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Locators.ERROR_PASSWORD))).text
        assert text_error == 'Некорректный пароль'
