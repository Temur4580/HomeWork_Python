import pytest
import sys
import os

# Добавляем путь к родительской папке task2_shop, чтобы найти pages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    """Тесты для интернет-магазина SauceDemo"""

    def test_shop_total_amount(self, driver):
        """
        Тест проверяет оформление заказа с тремя товарами
        Ожидаемая итоговая сумма: $58.29
        """
        # Авторизация
        login_page = LoginPage(driver)
        inventory_page = (login_page.open()
                          .enter_username("standard_user")
                          .enter_password("secret_sauce")
                          .click_login())

        # Добавление товаров в корзину
        (inventory_page.add_backpack_to_cart()
         .add_bolt_tshirt_to_cart()
         .add_onesie_to_cart())

        # Проверка, что в корзине 3 товара
        assert inventory_page.get_cart_item_count() == "3", "В корзине должно быть 3 товара"

        # Переход в корзину
        cart_page = inventory_page.go_to_cart()

        # Проверка содержимого корзины
        assert cart_page.get_cart_items_count() == 3, "В корзине должно быть 3 товара"

        # Переход к оформлению
        checkout_page = cart_page.click_checkout()

        # Заполнение формы
        (checkout_page.enter_first_name("Temur")
         .enter_last_name("Bilyalov")
         .enter_postal_code("123456")
         .click_continue())

        # Получение итоговой суммы
        total_text = checkout_page.get_total_amount()
        print(f"\nИтоговая сумма: {total_text}")

        # Проверка итоговой суммы
        expected_total = "Total: $58.29"
        assert total_text == expected_total, \
            f"Ожидалась сумма {expected_total}, получено {total_text}"

        # Завершение заказа
        checkout_page.click_finish()