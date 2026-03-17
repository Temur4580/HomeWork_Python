"""
Page Object для страницы корзины.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    """Страница корзины"""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_item_in_cart(self, item_name: str) -> bool:
        """Проверить наличие товара в корзине"""
        item_locator = (By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")
        try:
            self.find_element(item_locator)
            return True
        except:
            return False

    @allure.step("Удалить товар из корзины")
    def remove_item(self, item_name: str) -> 'CartPage':
        """Удалить товар из корзины"""
        remove_button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button")
        self.click(remove_button)
        return self

    def checkout(self) -> None:
        """Оформить заказ"""
        self.click(self.CHECKOUT_BUTTON)
