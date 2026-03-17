"""
Page Object для страницы товаров.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):
    """Страница товаров"""

    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def is_opened(self) -> bool:
        """Проверить, что страница открыта"""
        try:
            return self.get_text(self.TITLE) == "Products"
        except:
            return False

    @allure.step("Добавить товар")
    def add_item_to_cart(self, item_name: str):
        """Добавить товар в корзину"""
        add_button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(add_button)

    def get_cart_badge_count(self) -> str:
        """Получить количество товаров"""
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"
