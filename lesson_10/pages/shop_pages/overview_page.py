"""
Page Object для страницы обзора заказа перед подтверждением.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OverviewPage(BasePage):
    """
    Page Object для страницы обзора заказа.

    Attributes:
        FINISH_BUTTON: Локатор кнопки завершения заказа
    """

    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        """Инициализация страницы обзора заказа"""
        super().__init__(driver)

    @allure.step("Завершить оформление заказа")
    def finish_checkout(self) -> 'OverviewPage':
        """
        Нажать кнопку Finish для завершения заказа.

        Returns:
            OverviewPage: Экземпляр страницы
        """
        self.click(self.FINISH_BUTTON, timeout=10)
        return self