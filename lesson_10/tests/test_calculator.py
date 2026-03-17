"""
Тесты для страницы калькулятора с задержкой.
"""
import allure
import pytest
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор с задержкой")
@allure.story("Арифметические операции")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для страницы калькулятора с задержкой"""

    @allure.title("Тест сложения с задержкой 45 секунд")
    @allure.description("""
        Проверка корректности выполнения операции сложения 7 + 8 
        с установленной задержкой 45 секунд.

        Ожидаемый результат: 15
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "calculator", "addition")
    def test_calculator_addition_with_delay(self, driver):
        """
        Тест проверяет сложение 7 + 8 с задержкой 45 секунд.

        Test data:
            - Первое число: 7
            - Второе число: 8
            - Задержка: 45 секунд
            - Ожидаемый результат: 15
        """
        # Создаем объект страницы и открываем её
        calculator_page = CalculatorPage(driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввод выражения 7 + 8"):
            calculator_page.click_button("7") \
                .click_button("+") \
                .click_button("8") \
                .click_button("=")

        with allure.step("Ожидание результата вычисления"):
            calculator_page.wait_for_result("15", timeout=50)

        with allure.step("Получение и проверка результата"):
            result = calculator_page.get_result()

            with allure.step(f"Проверка: ожидалось '15', получено '{result}'"):
                assert result == "15", f"Ожидался результат 15, получено {result}"

            allure.attach(
                f"Результат вычисления: {result}",
                name="Результат теста",
                attachment_type=allure.attachment_type.TEXT
            )
