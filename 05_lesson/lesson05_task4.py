from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер Firefox
driver = webdriver.Firefox()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith
driver.find_element(By.ID, "username").send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Нажать кнопку Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Дать время для загрузки
time.sleep(2)

# Вывести текст с зеленой плашки в консоль
flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text)

# Пауза для визуальной проверки
time.sleep(2)

# Закрыть браузер (метод quit())
driver.quit()