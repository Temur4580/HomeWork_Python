"""
Пакет с Page Object классами для интернет-магазина.
"""
from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .overview_page import OverviewPage

__all__ = ['LoginPage', 'InventoryPage', 'CartPage', 'CheckoutPage', 'OverviewPage']
