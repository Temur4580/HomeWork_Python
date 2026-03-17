"""
Короткие тесты для интернет-магазина Saucedemo.
"""
import allure
from pages.shop_pages.login_page import LoginPage
from pages.shop_pages.inventory_page import InventoryPage


@allure.feature("Интернет-магазин")
class TestShop:
    """Быстрые тесты для магазина"""

    @allure.title("Тест авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, driver):
        """Проверка входа в систему"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_opened(), "Не удалось войти"

    @allure.title("Тест корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart(self, driver):
        """Проверка добавления товара"""
        # Логинимся
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавляем товар
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # Проверяем счетчик
        assert inventory_page.get_cart_badge_count() == "1", "Товар не добавился"
