import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Chrome
    """
    print("Настройка Chrome драйвера...")

    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    try:
        # Пробуем разные способы
        driver = None

        # Способ 1: Selenium Manager (встроенный)
        try:
            print("Пробуем Selenium Manager...")
            driver = webdriver.Chrome(options=chrome_options)
            print("Chrome запущен через Selenium Manager")
        except:
            print("Selenium Manager не сработал, пробуем webdriver-manager...")

            # Способ 2: webdriver-manager с явным указанием пути
            from webdriver_manager.chrome import ChromeDriverManager
            from webdriver_manager.core.os_manager import ChromeType

            try:
                chromedriver_path = ChromeDriverManager().install()
                print(f"webdriver-manager путь: {chromedriver_path}")

                # Проверяем, что файл существует и это .exe
                if chromedriver_path and os.path.exists(chromedriver_path):
                    if chromedriver_path.endswith('.exe'):
                        service = Service(executable_path=chromedriver_path)
                        driver = webdriver.Chrome(service=service, options=chrome_options)
                    else:
                        # Если это не .exe, ищем chromedriver.exe в той же папке
                        dir_path = os.path.dirname(chromedriver_path)
                        exe_path = os.path.join(dir_path, 'chromedriver.exe')
                        if os.path.exists(exe_path):
                            service = Service(executable_path=exe_path)
                            driver = webdriver.Chrome(service=service, options=chrome_options)
                        else:
                            raise Exception("chromedriver.exe не найден")
            except Exception as e:
                print(f"webdriver-manager ошибка: {e}")

                # Способ 3: Ручной путь (если вы сами скачали chromedriver)
                print("Пробуем ручной путь...")
                manual_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
                if os.path.exists(manual_path):
                    service = Service(executable_path=manual_path)
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                else:
                    # Способ 4: Просто без указания пути (найдет в PATH)
                    print("Пробуем без указания пути...")
                    driver = webdriver.Chrome(options=chrome_options)

        if driver is None:
            raise Exception("Не удалось запустить Chrome ни одним способом")

        print("Chrome успешно запущен")
        yield driver

    except Exception as e:
        print(f"Ошибка при запуске Chrome: {e}")
        raise
    finally:
        if 'driver' in locals() and driver:
            print("Закрытие браузера...")
            driver.quit()