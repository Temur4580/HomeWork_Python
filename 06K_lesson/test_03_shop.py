import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class TestSauceDemo:

    def setup_method(self):
        print("\n🔵 Запуск Firefox...")
        options = Options()
        options.add_argument("--start-maximized")

        # Явно указываем путь к Firefox (измените если нужно)
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        # Устанавливаем драйвер
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)

        # Увеличиваем таймауты
        self.driver.set_page_load_timeout(30)
        self.wait = WebDriverWait(self.driver, 15)

        print("🟡 Открытие сайта...")
        self.driver.get("https://www.saucedemo.com/")
        print("🟢 Сайт загружен!")
        time.sleep(1)  # Небольшая пауза для гарантии

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
            print("🔴 Браузер закрыт")

    def test_purchase(self):
        # Авторизация
        username = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")
        print("✅ Логин введен")

        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        print("✅ Пароль введен")

        self.driver.find_element(By.ID, "login-button").click()
        print("✅ Кнопка нажата")

        # Проверка что перешли на страницу товаров
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        print("✅ Страница товаров загружена")

        # Добавление товаров
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        print("✅ Backpack добавлен")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        print("✅ T-Shirt добавлен")
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        print("✅ Onesie добавлен")

        # Корзина
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("✅ Корзина открыта")

        # Checkout
        checkout = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout.click()
        print("✅ Checkout нажат")

        # Данные покупателя
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        print("✅ Данные заполнены")

        # Continue
        self.driver.find_element(By.ID, "continue").click()
        print("✅ Continue нажат")

        # Проверка суммы
        total = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        print(f"💰 Итоговая сумма: {total}")

        assert total == "Total: $58.29", f"Ожидалось $58.29, получено {total}"
        print("✅ ТЕСТ ПРОЙДЕН!")


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])