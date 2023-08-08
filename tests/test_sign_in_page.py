from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestSignInPage:
    def test_sign_in_by_enter_button(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_by_personal_account_page(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_from_registration_page(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj']").click() # Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click() # Кнопка "Войти"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        assert orders_link_text == 'Оформить заказ'

    def test_sign_in_from_password_recovery_page(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click() # Кнопка "Восстановить пароль"
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click() # Кнопка "Войти"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") #  Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        assert orders_link_text == 'Оформить заказ'






