"""
Тест для проверки работы ChromeDriver.
"""
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


@allure.feature("Проверка ChromeDriver")
@allure.title("Тест с прямым указанием пути")
def test_with_direct_path():
    """Тест с прямым указанием пути к ChromeDriver"""
    with allure.step("Настройка ChromeDriver"):
        options = Options()
        options.add_argument("--headless=new")  # Запуск в фоновом режиме
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Прямой путь к ChromeDriver
        chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"

        # Проверяем существование файла
        assert os.path.exists(chrome_driver_path), f"Файл не найден: {chrome_driver_path}"

        service = Service(chrome_driver_path)

    with allure.step("Запуск браузера"):
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открытие страницы"):
        driver.get("https://www.google.com")
        title = driver.title
        allure.attach(title, name="Заголовок страницы", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Закрытие браузера"):
        driver.quit()

    assert "Google" in title
