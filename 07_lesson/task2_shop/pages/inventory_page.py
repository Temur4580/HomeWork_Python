from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Page Object для главной страницы магазина (товары)"""

    # Локаторы для кнопок добавления товаров
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Локатор для корзины
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину"""
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        add_button.click()
        return self

    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку Bolt в корзину"""
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON)
        )
        add_button.click()
        return self

    def add_onesie_to_cart(self):
        """Добавить комбинезон в корзину"""
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON)
        )
        add_button.click()
        return self

    def get_cart_item_count(self) -> str:
        """Получить количество товаров в корзине"""
        try:
            cart_badge = self.wait.until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return cart_badge.text
        except:
            return "0"

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)