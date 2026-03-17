"""
Базовый класс для всех страниц приложения.
Содержит общие методы для работы со страницами.
"""
from typing import Optional, Any, Tuple
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:
    """
    Базовый класс Page Object, содержащий общие методы для всех страниц.

    Attributes:
        driver: WebDriver instance
        base_url: Базовый URL приложения
        wait: WebDriverWait instance для ожиданий
    """

    def __init__(self, driver: WebDriver, base_url: str = "http://localhost") -> None:
        """
        Инициализация базовой страницы.

        Args:
            driver: WebDriver instance для управления браузером
            base_url: Базовый URL приложения (по умолчанию "http://localhost")
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        """
        Найти элемент на странице с ожиданием его появления.

        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            WebElement: Найденный элемент

        Raises:
            TimeoutException: Если элемент не найден за указанное время
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable_element(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        """
        Найти кликабельный элемент на странице.

        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            WebElement: Кликабельный элемент
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> 'BasePage':
        """
        Кликнуть по элементу.

        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Максимальное время ожидания

        Returns:
            BasePage: Экземпляр страницы для цепочки вызовов
        """
        element = self.find_clickable_element(locator, timeout)
        element.click()
        return self

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(self, locator: Tuple[str, str], text: str, timeout: Optional[int] = None) -> 'BasePage':
        """
        Ввести текст в элемент.

        Args:
            locator: Кортеж (By, selector) для поиска элемента
            text: Текст для ввода
            timeout: Максимальное время ожидания

        Returns:
            BasePage: Экземпляр страницы для цепочки вызовов
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> str:
        """
        Получить текст элемента.

        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Максимальное время ожидания

        Returns:
            str: Текст элемента
        """
        element = self.find_element(locator, timeout)
        text = element.text
        allure.attach(text, name="Текст элемента", attachment_type=allure.attachment_type.TEXT)
        return text
