"""
Page Object для страницы авторизации интернет-магазина.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """
    Page Object для страницы авторизации.

    Attributes:
        USERNAME_INPUT: Локатор поля ввода имени пользователя
        PASSWORD_INPUT: Локатор поля ввода пароля
        LOGIN_BUTTON: Локатор кнопки входа
        ERROR_MESSAGE: Локатор сообщения об ошибке
    """

    # Локаторы элементов страницы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, "https://www.saucedemo.com/")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открыть страницу авторизации.

        Returns:
            LoginPage: Экземпляр страницы
        """
        self.driver.get(self.base_url)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """
        Ввести имя пользователя.

        Args:
            username: Имя пользователя

        Returns:
            LoginPage: Экземпляр страницы
        """
        self.input_text(self.USERNAME_INPUT, username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> 'LoginPage':
        """
        Ввести пароль.

        Args:
            password: Пароль пользователя

        Returns:
            LoginPage: Экземпляр страницы
        """
        self.input_text(self.PASSWORD_INPUT, password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> 'LoginPage':
        """
        Нажать кнопку входа.

        Returns:
            LoginPage: Экземпляр страницы
        """
        self.click(self.LOGIN_BUTTON)
        return self

    @allure.step("Выполнить вход с учетными данными: {username}")
    def login(self, username: str, password: str) -> 'LoginPage':
        """
        Выполнить полный процесс авторизации.

        Args:
            username: Имя пользователя
            password: Пароль

        Returns:
            LoginPage: Экземпляр страницы
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self) -> str:
        """
        Получить текст сообщения об ошибке.

        Returns:
            str: Текст ошибки или пустая строка
        """
        return self.get_text(self.ERROR_MESSAGE)
