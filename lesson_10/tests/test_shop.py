"""
Тесты для интернет-магазина Saucedemo.
"""
import allure
import pytest
from pages.shop_pages.login_page import LoginPage
from pages.shop_pages.inventory_page import InventoryPage
from pages.shop_pages.cart_page import CartPage
from pages.shop_pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
class TestShop:
    """Тесты для интернет-магазина"""

    @allure.title("Тест авторизации")
    @allure.description("Проверка входа в систему")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, driver):
        """Тест проверяет успешный вход в систему"""
        with allure.step("Открыть страницу авторизации"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Ввести логин и пароль"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Проверить, что вход выполнен"):
            inventory_page = InventoryPage(driver)
            assert inventory_page.is_opened(), "Не удалось войти в систему"

    @allure.title("Тест добавления товара в корзину")
    @allure.description("Проверка добавления и удаления товара")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_operations(self, driver):
        """Тест проверяет операции с корзиной"""
        # Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавление товара
        inventory_page = InventoryPage(driver)
        with allure.step("Добавить товар в корзину"):
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            assert inventory_page.get_cart_badge_count() == "1"

        # Переход в корзину и проверка
        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()
            cart_page = CartPage(driver)
            assert cart_page.is_item_in_cart("Sauce Labs Backpack")

        # Удаление товара
        with allure.step("Удалить товар из корзины"):
            cart_page.remove_item("Sauce Labs Backpack")
            assert not cart_page.is_item_in_cart("Sauce Labs Backpack")

    @allure.title("Тест полной покупки")
    @allure.description("Проверка полного цикла покупки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_purchase(self, driver):
        """Тест проверяет полный процесс покупки"""
        # Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавление товара
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # Оформление заказа
        inventory_page.go_to_cart()
        cart_page = CartPage(driver)

        with allure.step("Оформить заказ"):
            cart_page.checkout()
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_customer_info("John", "Doe", "12345")
            checkout_page.continue_checkout()
            checkout_page.finish_checkout()

            assert checkout_page.is_checkout_complete(), "Заказ не оформлен"
