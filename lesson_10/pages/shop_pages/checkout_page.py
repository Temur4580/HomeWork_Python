"""
Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    COMPLETE_CONTAINER = (By.ID, "checkout_complete_container")

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
            # Ждем появления контейнера с подтверждением
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.COMPLETE_CONTAINER)
            )

            # Проверяем текст сообщения
            message = self.get_text(self.SUCCESS_MESSAGE)
            allure.attach(f"Сообщение: {message}", name="Успешное оформление",
                          attachment_type=allure.attachment_type.TEXT)
            return True
        except Exception as e:
            allure.attach(str(e), name="Ошибка проверки",
                          attachment_type=allure.attachment_type.TEXT)
            return False
