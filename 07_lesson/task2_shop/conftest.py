import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    """
    Фикстура для Firefox с автоматической загрузкой драйвера
    """
    print("Настройка Firefox драйвера...")

    # Настройка опций Firefox
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")

    try:
        # Автоматическая загрузка и установка geckodriver
        print("Загрузка geckodriver...")
        geckodriver_path = GeckoDriverManager().install()
        print(f"Geckodriver установлен по пути: {geckodriver_path}")

        # Создание сервиса с драйвером
        service = Service(executable_path=geckodriver_path)

        # Создание экземпляра драйвера Firefox
        print("Запуск Firefox...")
        driver = webdriver.Firefox(service=service, options=firefox_options)
        print("Firefox успешно запущен")

        # Передаем драйвер тесту
        yield driver

    except Exception as e:
        print(f"Ошибка при запуске Firefox: {e}")
        raise
    finally:
        # Закрываем браузер после завершения теста
        if 'driver' in locals():
            print("Закрытие браузера...")
            driver.quit()