from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestConstructorPage:
    def test_click_sauces(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//span[text()='Соусы']"))) # Кнопка соусы
        driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Соусы']"))).text # Заголовок соусы
        assert expected_text == 'Соусы'

    def test_click_fillings(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//span[text()='Начинки']"))) # Кнопка начинки
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Начинки']"))).text # Заголовок начинки
        assert expected_text == 'Начинки'

    def test_click_rolls(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//span[text()='Начинки']"))) # Кнопка начинки
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Булки']"))).text # Кнопка Булкив
        assert expected_text == 'Булки'