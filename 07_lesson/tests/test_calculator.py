import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    """Тесты для страницы калькулятора"""

    def test_calculator_addition_with_delay(self, driver):
        """
        Тест проверяет сложение 7 + 8 с задержкой 45 секунд
        Ожидаемый результат: 15 через 45 секунд
        """
        # Создаем объект страницы и открываем её
        calculator_page = CalculatorPage(driver)
        calculator_page.open()

        # Устанавливаем задержку 45 секунд
        calculator_page.set_delay(45)

        # Выполняем вычисления: 7 + 8 =
        calculator_page.click_button("7") \
            .click_button("+") \
            .click_button("8") \
            .click_button("=")

        # Ждем результат 15 (с учетом установленной задержки)
        calculator_page.wait_for_result("15", timeout=50)

        # Получаем результат и проверяем его
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат 15, получено {result}"