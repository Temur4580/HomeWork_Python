from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Базовое ожидание

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds: int):
        """Установить задержку в секундах"""
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, button_text: str):
        """Нажать на кнопку калькулятора"""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        return self

    def get_result(self) -> str:
        """Получить результат вычисления"""
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_DISPLAY)
        )
        return result_element.text

    def wait_for_result(self, expected_result: str, timeout: int = None):
        """Ожидать появления ожидаемого результата"""
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait

        wait.until(
            EC.text_to_be_present_in_element(self.RESULT_DISPLAY, expected_result)
        )
        return self