import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


class TestSlowCalculator:
    """Тест для проверки медленного калькулятора с задержкой 45 секунд"""

    def setup_method(self):
        """Настройка браузера Chrome перед каждым тестом"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Автоматическое управление драйвером Chrome
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Увеличим таймаут для ожидания результата
        self.wait = WebDriverWait(self.driver, 50)

    def teardown_method(self):
        """Завершение работы браузера после теста"""
        if self.driver:
            self.driver.quit()

    def test_calculator_with_delay(self):
        """Тест проверяет вычисление 7 + 8 с задержкой 45 секунд"""

        # 1. Устанавливаем задержку 45 секунд
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 2. Нажимаем кнопки: 7, +, 8, =
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 3. Ожидаем появления результата 15 в окне калькулятора
        # Локатор для окна результата (верхнее поле)
        result_locator = (By.CSS_SELECTOR, ".screen")

        try:
            # Ждем, пока текст в элементе станет равен "15"
            result_element = self.wait.until(
                EC.text_to_be_present_in_element(result_locator, "15")
            )
            # Получаем фактический текст для проверки
            actual_result = self.driver.find_element(*result_locator).text
            assert actual_result == "15", f"Ожидался результат 15, но получен {actual_result}"
            print(f"\n✅ Результат '{actual_result}' получен в течение 50 секунд.")

        except TimeoutException:
            # Если результат не появился за 50 секунд
            actual_result = self.driver.find_element(*result_locator).text
            pytest.fail(f"Результат не появился за 50 секунд. Текущее значение: '{actual_result}'")

if __name__ == "__main__":
    pytest.main(["-v", __file__])