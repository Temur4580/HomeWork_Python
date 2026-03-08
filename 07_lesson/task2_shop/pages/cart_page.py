from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object для страницы корзины"""

    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self) -> list:
        """Получить список названий товаров в корзине"""
        item_elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [item.text for item in item_elements]

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)