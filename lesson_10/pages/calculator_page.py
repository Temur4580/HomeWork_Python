"""
Page Object для страницы калькулятора с задержкой.
"""
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
import allure


class CalculatorPage(BasePage):
    """
    Page Object для страницы калькулятора с задержкой.

    Attributes:
        DELAY_INPUT: Локатор поля ввода задержки
        RESULT_DISPLAY: Локатор дисплея результата
    """

    # Локаторы элементов страницы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance для управления браузером
        """
        super().__init__(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> 'CalculatorPage':
        """
        Открыть страницу калькулятора в браузере.

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        with allure.step(f"Переход по URL: {self.base_url}"):
            self.driver.get(self.base_url)
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> 'CalculatorPage':
        """
        Установить задержку вычислений в секундах.

        Args:
            seconds: Количество секунд задержки

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.input_text(self.DELAY_INPUT, str(seconds))
        return self

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Нажать на кнопку калькулятора с указанным текстом.

        Args:
            button_text: Текст на кнопке (цифра или оператор)

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.click(button_locator)
        return self

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Получить текущее значение на дисплее калькулятора.

        Returns:
            str: Текст, отображаемый на дисплее калькулятора
        """
        return self.get_text(self.RESULT_DISPLAY)

    @allure.step("Ожидать результат '{expected_result}'")
    def wait_for_result(self, expected_result: str, timeout: Optional[int] = None) -> 'CalculatorPage':
        """
        Ожидать появления ожидаемого результата на дисплее.

        Args:
            expected_result: Ожидаемое значение на дисплее
            timeout: Максимальное время ожидания в секундах

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        with allure.step(f"Ожидание появления текста '{expected_result}' на дисплее"):
            wait.until(
                EC.text_to_be_present_in_element(self.RESULT_DISPLAY, expected_result)
            )

        return self
