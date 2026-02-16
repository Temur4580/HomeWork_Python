from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest


class TestSlowCalculator:
    """Тесты для проверки калькулятора с задержкой"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        options = Options()
        options.add_argument("--start-maximized")
        # Опционально: запуск в headless режиме
        # options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)  # Базовое ожидание для поиска элементов
        self.wait = WebDriverWait(self.driver, 50)  # Основное ожидание с таймаутом 50 секунд

    def teardown_method(self):
        """Очистка после каждого теста"""
        if self.driver:
            self.driver.quit()

    def test_slow_calculator(self):
        """Тест проверки калькулятора с задержкой вычислений"""

        # Шаг 1: Открыть страницу калькулятора
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Шаг 2: Ввести значение 45 в поле задержки
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: Нажать кнопку 7
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()

        # Шаг 4: Нажать кнопку +
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()

        # Шаг 5: Нажать кнопку 8
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()

        # Шаг 6: Нажать кнопку =
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Шаг 7: Проверить, что результат отобразится через 45 секунд
        # Используем явное ожидание для проверки результата
        result_element = self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Дополнительная проверка через assert
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", f"Ожидался результат '15', но получен '{result_text}'"

        print("\n✓ Результат '15' успешно отобразился после задержки")


if __name__ == "__main__":
    pytest.main(["-v", __file__])