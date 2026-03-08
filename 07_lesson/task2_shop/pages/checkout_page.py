from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    # Локаторы для формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Локаторы для итоговой страницы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name: str):
        """Ввести имя"""
        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        return self

    def enter_last_name(self, last_name: str):
        """Ввести фамилию"""
        last_name_field = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code: str):
        """Ввести почтовый индекс"""
        postal_code_field = self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE_INPUT)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        return self

    def click_continue(self):
        """Нажать кнопку Continue"""
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_btn.click()
        return self

    def get_total_amount(self) -> str:
        """Получить итоговую сумму"""
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text

    def click_finish(self):
        """Нажать кнопку Finish (завершить заказ)"""
        finish_btn = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        finish_btn.click()
        return self