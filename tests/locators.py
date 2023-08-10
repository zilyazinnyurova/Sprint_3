from selenium.webdriver.common.by import By
class Locators:
    NAME_FIELD = (By.XPATH, ".//label[.='Имя']/following-sibling::input")  # Поле вода имени
    EMAIL_FIELD = (By.XPATH, ".//label[.='Email']/following-sibling::input")  # Поле вода email
    PASSWORD_FIELD = (By.XPATH, ".//label[.='Пароль']/following-sibling::input")  # Поле вода пароля
    BUTTON_ENTER_IN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']") # Кнопка для перехода в "Личный кабинет"
    BUTTON_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" на странице регистрации
    LINK_REGISTER = (By.XPATH, ".//a[@class='Auth_link__1fOlj']")  # Ссылка на страницу регистрации
    BUTTON_SIGN_IN = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    LINK_SIGN_IN = (By.XPATH, ".//a[text()='Войти']")  # Ссылка на страницу "Входа"
    BUTTON_SIGN_OUT = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход"
    TITLE_LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # Локатор для поиска заголовка 'Вход'
    ERROR_PASSWORD = (By.XPATH,".//p[(text()='Некорректный пароль')]") # Локатор для поиска текста 'Некорректный пароль'
    BUTTON_SAUCE = (By.XPATH, ".//span[text()='Соусы']") # Кнопка "Соусы"
    TITLE_SAUCE = (By.XPATH, ".//h2[text()='Соусы']") # Локатор для поиска заголовка 'Соусы'
    BUTTON_FILLINGS = (By.XPATH, ".//span[text()='Начинки']") # Кнопка "Начинки"
    TITLE_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']") # Локатор для поиска заголовка 'Начинки'
    BUTTON_ROLLS = (By.XPATH, ".//span[text()='Булки']")  # Кнопка "Булки"
    TITLE_ROLLS = (By.XPATH, ".//h2[text()='Булки']") # Локатор для поиска заголовка 'Начинки'
    BUTTON_MAKE_AN_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка "Конструктор"
    TEXT_ON_PAGE_PERSONAL_ACCOUNT = (By.XPATH, ".//p[contains(@class,'Account_text')]") # Локатор для поиска текста "В этом разделе вы можете изменить свои персональные данные" в личном кабинете.
    LOGO_STELLAR_BURGERS = (By.XPATH, ".//div[contains(@class,'logo')]") # Локатор для логотипа 'STELLAR BURGERS'
    LINK_RESTORE_PASSWORD_ON_PAGE_LOGIN = (By.XPATH, ".//a[text()='Восстановить пароль']") # Кнопка "Восстановить пароль" на странице входа


