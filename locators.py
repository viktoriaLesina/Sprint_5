from selenium.webdriver.common.by import By

# Главная страница
MAIN_PAGE_URL = "https://qa-desk.education-services.ru/"
# Кнопка Вход и регистрация

LOGIN_AND_REGISTRATION_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Вход и регистрация']",
)

# Поле имейл
EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name = 'email']")

# Поле пароль
PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name = 'password']")

# Кнопка Нет аккаунта
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")

# Кнопка Создать аккаунт
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")

# Кнопка Войти
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

# Кнопка Выйти
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

# Кнопка Повторите пароль
PASSWORD_SUBMIT_INPUT_FIELD = (By.XPATH, "//input[@name = 'submitPassword']")

# Кнопка Разместить объявление
CREATE_ADD = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")

# Модальное окно Разместить объявление без авторизации
CREATE_ADD_POPUP_USER_NOT_AUTHORIZED = (
    By.XPATH,
    "//form[contains(@class,'popUp_shell')]",
)

# Модальное окно Разместить объявление без авторизации заголовок
POPUP_TITLE_USER_NOT_AUTHORIZED = (
    By.XPATH,
    "//form[contains(@class,'popUp_shell')]//h1[contains(., 'Чтобы разместить объявление')]",
)
# Аватар пользователя
USER_AVATAR = (By.XPATH, "//button[@class = 'circleSmall']")

# Имя пользователя
USER_NAME = (By.XPATH, "//h3[@class = 'profileText name']")

# Форма создания объявления
# Поле ввода Наздания товара
ITEM_NAME_INPUT_FIELD = (By.XPATH, "//input[@name = 'name']")

#Поле Категория
ITEM_CATEGORY_INPUT_FIELD = (By.XPATH, "//input[@name = 'category']")

#Выбор города из дропдауна
ITEM_CITY_ENTITY = (By.XPATH, "//span[text()='Санкт-Петербург']")

#Выбор категории
ITEM_CATEGORY_ENTITY = (By.XPATH, "//span[text()='Книги']")
# Поле Город
ITEM_CITY_FIELD = (By.XPATH, "//input[@name = 'city']")

# Кнопка Раскрыть дропдаун город
ITEM_CITY_ARROW_BUTTON = (
    By.XPATH,
    "//*[@name='category']/following::button[contains(@class, 'dropDownMenu_arrowDown')][2]",
)
# Кнопка Раскрыть дропдаун категория товара
ITEM_CATEGORY_ARROW_BUTTON = (
    By.XPATH,
    "//*[@name='category']/following::button[contains(@class, 'dropDownMenu_arrowDown')][1]",
)

# Радиобаттон состояние товара Б/У
ITEM_CONDITION_RADDIO_BUTTON_USED = (
    By.XPATH,
    "//div[contains(@class, 'radioUnput')][.//input[@value='Б/У']]",
)

# Поле ввода Описания товара
ITEM_DESCRIPTION_INPUT_FIELD = (By.XPATH, "//textarea[@name='description']")

# Поле ввода Цены товара
ITEM_PRICE_INPUT_FIELD = (By.XPATH, "//input[@name='price']")

# Кнопка Опубликовать
ITEM_PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

# Блок Мои объявления
USER_ADDS_SECTION = (
    By.XPATH,
    "//div[contains(@class, 'profilePage_listningBlock')]//h1[contains(., 'Мои объявления')]",
)

# Обявление в блоке Мои объявления
USER_ADD_CREATED_CARD = (By.XPATH, "//div[contains(@class, 'card')]")


# Errors
ERROR_FIELD_CLASS = "input_inputError"

ERROR_TEXT = (
    By.XPATH,
    "//*[contains(text(),'Ошибка')]"
)