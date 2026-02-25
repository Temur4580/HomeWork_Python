from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации"""

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username: str):
        """Ввести имя пользователя"""
        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password: str):
        """Ввести пароль"""
        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Нажать кнопку входа"""
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)