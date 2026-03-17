"""
Фикстуры для тестов с автоматическим поиском ChromeDriver.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import allure
from typing import Generator


def find_chromedriver():
    """
    Поиск ChromeDriver в различных местах.

    Returns:
        str: Путь к ChromeDriver или None
    """
    possible_paths = [
        "C:\\chromedriver\\chromedriver.exe",
        "C:\\Windows\\System32\\chromedriver.exe",
        os.path.expanduser("~\\chromedriver.exe"),
        os.path.expanduser("~\\AppData\\Local\\chromedriver.exe"),
        "chromedriver.exe",  # Будет искать в PATH
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    # Пробуем найти через where
    import subprocess
    try:
        result = subprocess.run(['where', 'chromedriver'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]
    except:
        pass

    return None


@pytest.fixture
def driver() -> Generator[webdriver.Chrome, None, None]:
    """
    Фикстура для создания и закрытия WebDriver.

    Returns:
        Generator[webdriver.Chrome]: Экземпляр WebDriver
    """
    with allure.step("Настройка и запуск браузера Chrome"):
        options = Options()

        # Базовые настройки
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")

        # Для отладки используем headless режим
        options.add_argument("--headless=new")

        # Путь к Chrome
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            options.binary_location = chrome_path

        # Ищем ChromeDriver
        chromedriver_path = find_chromedriver()

        if chromedriver_path:
            allure.attach(
                f"ChromeDriver найден: {chromedriver_path}",
                name="Информация",
                attachment_type=allure.attachment_type.TEXT
            )
            service = Service(chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            # Пробуем без указания пути (должен быть в PATH)
            allure.attach(
                "ChromeDriver не найден, пробуем стандартный способ",
                name="Предупреждение",
                attachment_type=allure.attachment_type.TEXT
            )
            driver = webdriver.Chrome(options=options)

        allure.attach(
            f"Браузер Chrome запущен",
            name="Информация о запуске",
            attachment_type=allure.attachment_type.TEXT
        )

        driver.implicitly_wait(5)

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()
