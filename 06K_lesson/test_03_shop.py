from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_saucedemo_total():
    """Тест проверки итоговой суммы в корзине SauceDemo"""

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    try:
        # Шаг 1: Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ожидание загрузки страницы товаров
        wait.until(EC.url_contains("inventory.html"))

        # Шаг 3: Добавление товаров в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Шаг 4: Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("cart.html"))

        # Шаг 5: Нажать Checkout
        driver.find_element(By.ID, "checkout").click()

        # Шаг 6: Заполнить форму
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Шаг 7: Нажать Continue
        driver.find_element(By.ID, "continue").click()

        # Шаг 8: Получить итоговую сумму
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_value = total_text.replace("Total: $", "").strip()

        # Шаг 9: Проверка итоговой суммы
        expected_total = "58.29"
        assert total_value == expected_total, f"Ожидалась сумма ${expected_total}, получена ${total_value}"

        print(f"\n✓ Итоговая сумма: ${total_value} - тест пройден!")

    finally:
        # Шаг 10: Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", __file__])