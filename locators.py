from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    field_name = (By.XPATH, "(//input[@name='name'])[1]")
    field_email = (By.XPATH, "(//input[@name='name'])[2]")
    field_password = (By.NAME, "Пароль")
    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ошибка при вводе некорректного пароля
    error_password = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Ошибка под полем пароля

    # Главная страница
    logo = (By.XPATH, "//header/nav/div")  # Логотип.
    button_login_main = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка 'Войти в аккаунт' на главной странице.
    link_constructor = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Ссылка 'Конструктор' на главной странице.
    link_personal_area = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Ссылка 'Личный кабинет' на главной странице.

    # Вход с главной страницы
    field_email_login = (By.XPATH, "//input[@name='name' and @type='text']")  # Поле ввода 'Email' при входе.
    field_password_login = (By.XPATH, "//input[@name='Пароль' and @type='password']")  # Поле ввода 'Пароль' при входе.
    button_login = (By.XPATH, "//button[text()='Войти']")  # Кнопка 'Войти'.

    # Кнопки для регистрации и восстановления пароля
    button_go_to_register = (By.XPATH, "//a[@href='/register']")  # Кнопка 'Зарегистрироваться' через форму входа.
    button_forgot_password = (By.XPATH, "//a[@href='/forgot-password']")  # Кнопка 'Восстановить пароль'.
    button_go_to_login_from_register = (By.XPATH, "//a[@href='/login']")  # Кнопка 'Войти' через форму регистрации.
    button_go_to_login_from_forgot_password = (By.XPATH, "//a[@href='/login']")  # Кнопка 'Войти' через форму восстановления пароля.

    # Личный кабинет
    button_exit_personal_area = (By.XPATH, "//button[text()='Выход']")  # Кнопка 'Выход' из личного кабинета.

    # Вкладки
    tab_buns = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")  # Вкладка 'Булки'.
    tab_sauces = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")  # Вкладка 'Соусы'.
    tab_fillings = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")  # Вкладка 'Начинки'.

    # Активные вкладки
    active_tab_buns = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")  # Активная вкладка 'Булки'.
    active_tab_sauces = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")  # Активная вкладка 'Соусы'.
    active_tab_fillings = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")  # Активная вкладка 'Начинки'.