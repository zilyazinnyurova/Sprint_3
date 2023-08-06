import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestRegistrationPage:
    def test_registration(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click() # Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Зиля") # Поле вода имени
        rand = random.randint(900, 999)
        email = "zilya_zinnyurova_12_" + str(rand) + "@gmail.com"
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys(email) #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div[1]/div[1]/input[1]").send_keys("11%gjcRsx#ilo") #  Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"
        title_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']"))).text # Находим текст
        assert title_text == 'Вход'

    def test_registration_password_entry_error(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click() # Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Зиля") # Поле вода имени
        rand = random.randint(900, 999)
        email = "zilya_zinnyurova_12_" + str(rand) + "@gmail.com"
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys(email) #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div[1]/div[1]/input[1]").send_keys("1eh3") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"
        text_error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[(text()='Некорректный пароль')]"))).text  # Находим кнопку
        assert text_error == 'Некорректный пароль'
