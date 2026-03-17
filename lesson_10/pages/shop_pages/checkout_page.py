"""
Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    @allure.step("Заполнить информацию")
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """Заполнить информацию о покупателе"""
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)
        return self

    @allure.step("Продолжить оформление")
    def continue_checkout(self) -> 'CheckoutPage':
        """Нажать кнопку Continue"""
        self.click(self.CONTINUE_BUTTON)
        return self

    def is_checkout_complete(self) -> bool:
        """Проверить, что заказ оформлен"""
        try:
            self.find_element(self.SUCCESS_MESSAGE, timeout=5)
            return True
        except:
            return False
