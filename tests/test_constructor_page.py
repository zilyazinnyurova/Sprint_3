from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestConstructorPage:
    def test_click_sauces(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_SAUCE)))
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.TITLE_SAUCE))).text
        assert expected_text == 'Соусы'

    def test_click_fillings(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_FILLINGS)))
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.TITLE_FILLINGS))).text
        assert expected_text == 'Начинки'

    def test_click_rolls(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.BUTTON_FILLINGS)))
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        driver.find_element(*Locators.BUTTON_ROLLS).click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((Locators.TITLE_ROLLS))).text
        assert expected_text == 'Булки'