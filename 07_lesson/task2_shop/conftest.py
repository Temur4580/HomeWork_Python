import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os
import time


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Firefox
    """
    print("\nНастройка Firefox драйвера...")

    # Настройка опций Firefox
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")

    # Важно: добавляем эти настройки для стабильности
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    # Настройки для избежания конфликтов
    firefox_options.set_preference("dom.ipc.plugins.enabled", False)
    firefox_options.set_preference("browser.tabs.remote.autostart", False)
    firefox_options.set_preference("browser.tabs.remote.autostart.2", False)

    try:
        # Способ 1: Selenium Manager (встроенный)
        try:
            print("Пробуем Selenium Manager...")
            driver = webdriver.Firefox(options=firefox_options)
            print("Firefox запущен через Selenium Manager")

        except Exception as e:
            print(f"Selenium Manager не сработал: {e}")
            print("Пробуем webdriver-manager...")

            # Способ 2: webdriver-manager
            geckodriver_path = GeckoDriverManager().install()
            print(f"Geckodriver путь: {geckodriver_path}")

            # Проверяем, что файл существует
            if not os.path.exists(geckodriver_path):
                # Ищем geckodriver.exe в той же папке
                geckodriver_dir = os.path.dirname(geckodriver_path)
                geckodriver_exe = os.path.join(geckodriver_dir, "geckodriver.exe")
                if os.path.exists(geckodriver_exe):
                    geckodriver_path = geckodriver_exe
                else:
                    # Ищем в папке проекта
                    project_dir = os.path.dirname(os.path.abspath(__file__))
                    geckodriver_exe = os.path.join(project_dir, "geckodriver.exe")
                    if os.path.exists(geckodriver_exe):
                        geckodriver_path = geckodriver_exe

            print(f"Используем geckodriver: {geckodriver_path}")

            service = Service(executable_path=geckodriver_path)
            driver = webdriver.Firefox(service=service, options=firefox_options)

        print("Firefox успешно запущен")
        yield driver

    except Exception as e:
        print(f"Ошибка при запуске Firefox: {e}")
        print("\nВозможные решения:")
        print("1. Закройте все окна Firefox")
        print("2. Перезагрузите компьютер")
        print("3. Проверьте версию Firefox (должна быть совместима с geckodriver 0.36.0)")
        raise
    finally:
        print("Закрытие браузера...")
        if 'driver' in locals():
            driver.quit()