"""
Page Object для страницы обзора заказа перед подтверждением.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import allure
import time


class OverviewPage(BasePage):
    """
    Page Object для страницы обзора заказа.

    Attributes:
        FINISH_BUTTON: Локатор кнопки завершения заказа
        CANCEL_BUTTON: Локатор кнопки отмены
        SUMMARY_TOTAL: Локатор итоговой суммы
    """

    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """Инициализация страницы обзора заказа"""
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)  # Увеличиваем таймаут до 20 секунд

    @allure.step("Ожидать загрузку страницы обзора")
    def wait_for_page_load(self) -> bool:
        """
        Ожидать загрузки страницы обзора заказа.

        Returns:
            bool: True если страница загружена, False если нет
        """
        try:
            # Ждем изменения URL
            self.wait.until(
                EC.url_contains("checkout-step-two"),
                message="URL не содержит 'checkout-step-two'"
            )

            # Ждем появления кнопки Finish
            self.wait.until(
                EC.presence_of_element_located(self.FINISH_BUTTON),
                message="Кнопка Finish не появилась"
            )

            # Дополнительная проверка - кнопка должна быть видимой
            self.wait.until(
                EC.visibility_of_element_located(self.FINISH_BUTTON),
                message="Кнопка Finish не видима"
            )

            allure.attach(
                "Страница обзора успешно загружена",
                name="Статус загрузки",
                attachment_type=allure.attachment_type.TEXT
            )
            return True

        except TimeoutException as e:
            # Делаем скриншот при ошибке
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Скриншот ошибки загрузки страницы",
                attachment_type=allure.attachment_type.PNG
            )

            # Сохраняем текущий URL для отладки
            current_url = self.driver.current_url
            allure.attach(
                current_url,
                name="Текущий URL при ошибке",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                str(e),
                name="Детали ошибки",
                attachment_type=allure.attachment_type.TEXT
            )
            return False

    @allure.step("Завершить оформление заказа")
    def finish_checkout(self) -> 'OverviewPage':
        """
        Нажать кнопку Finish для завершения заказа.

        Returns:
            OverviewPage: Экземпляр страницы

        Raises:
            TimeoutException: Если кнопка Finish не стала кликабельной
        """
        # Ждем загрузки страницы
        if not self.wait_for_page_load():
            # Если страница не загрузилась, пробуем еще раз с увеличенным таймаутом
            time.sleep(2)  # Небольшая пауза
            self.wait = WebDriverWait(self.driver, 30)
            self.wait_for_page_load()

        # Делаем скриншот перед кликом
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Страница обзора перед завершением",
            attachment_type=allure.attachment_type.PNG
        )

        # Проверяем итоговую сумму (опционально)
        try:
            total = self.get_text(self.SUMMARY_TOTAL)
            allure.attach(
                f"Итоговая сумма: {total}",
                name="Информация о заказе",
                attachment_type=allure.attachment_type.TEXT
            )
        except:
            pass

        # Кликаем по кнопке Finish с увеличенным таймаутом
        with allure.step("Клик по кнопке Finish"):
            self.click(self.FINISH_BUTTON, timeout=15)

        # Проверяем, что клик сработал (опционально)
        time.sleep(1)

        return self

    @allure.step("Отменить оформление заказа")
    def cancel_checkout(self) -> 'OverviewPage':
        """
        Нажать кнопку Cancel для отмены заказа.

        Returns:
            OverviewPage: Экземпляр страницы
        """
        self.click(self.CANCEL_BUTTON)
        return self

    @allure.step("Получить итоговую сумму")
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму заказа.

        Returns:
            str: Текст с итоговой суммой
        """
        return self.get_text(self.SUMMARY_TOTAL)
