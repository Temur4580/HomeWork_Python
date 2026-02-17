import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


class TestFormValidation:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(options=options)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):
        self.driver.quit()

    def test_form_validation(self):
        # Сначала посмотрим какие ID есть на странице (для отладки)
        print("\nДоступные элементы на странице:")
        elements = self.driver.find_elements(By.CSS_SELECTOR, "input, select, textarea")
        for el in elements:
            try:
                print(
                    f"ID: {el.get_attribute('id')}, Name: {el.get_attribute('name')}, Type: {el.get_attribute('type')}")
            except:
                pass

        # Данные для формы - используем name атрибуты если ID не работают
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполнение формы по name атрибуту
        for field_name, value in data.items():
            try:
                # Пробуем найти по ID
                field = self.driver.find_element(By.ID, field_name)
            except:
                # Если не нашли по ID, пробуем по name
                field = self.driver.find_element(By.NAME, field_name)

            field.clear()
            if value:
                field.send_keys(value)

        # Отправка
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ожидание подсветки
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success")))

        # Проверки
        zip_field = self.driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_field.get_attribute("class"), "Zip code должен быть красным"

        for field_name in [f for f in data.keys() if f != "zip-code"]:
            field = self.driver.find_element(By.ID, field_name)
            assert "alert-success" in field.get_attribute("class"), f"{field_name} должен быть зеленым"


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])  # -s для вывода print
