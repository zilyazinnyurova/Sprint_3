from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestSignOutPage:
    def test_sign_in_by_enter_button(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") # Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click() # Кнопка "Личный Кабинет"
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"))).text # Находим кнопку
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click() # Кнопка "Выход"
        expected_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти']"))).text # Находим кнопку
        assert expected_text == 'Войти'