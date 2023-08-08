from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestGoToConstructorPage:
    def test_click_to_go_to_constructor(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") # Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click() # Кнопка для перехода в личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//p[contains(@class,'Account_text')]"))).text # Находим кнопку
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click() # Кнопка "Конструктор"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Поиск кнопки оформить заказ
        assert orders_link_text == 'Оформить заказ'


    # еще логотип Stellar Burgers

    def test_click_to_go_to_stellar_burgers(self, driver):
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() # Кнопка "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div[1]/div[1]/input[1]").send_keys("zilya_zinnyurova_12_999@gmail.com") # Поле вода email
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div[1]/div[1]/input[1]").send_keys("jhg35TRFw") # Поле вода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Находим кнопку
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click() # Кнопка для перехода в личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//p[contains(@class,'Account_text')]"))).text # Находим текст
        driver.find_element(By.XPATH, ".//div[contains(@class,'logo')]").click() # Кнопка для перехода по клику на логотип "Stellar Burgers"
        orders_link_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))).text # Поиск кнопки оформить заказ
        assert orders_link_text == 'Оформить заказ'