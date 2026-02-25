import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера браузера
    """
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Открыть браузер на весь экран

    # Создание экземпляра драйвера
    driver = webdriver.Chrome(options=chrome_options)

    # Передаем драйвер тесту
    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()