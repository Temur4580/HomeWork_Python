from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер Firefox
driver = webdriver.Firefox()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввести "Sky"
input_field.send_keys("Sky")

# Пауза для наглядности
time.sleep(1)

# Очистить поле
input_field.clear()

# Пауза для наглядности
time.sleep(1)

# Ввести "Pro"
input_field.send_keys("Pro")

# Пауза чтобы увидеть результат
time.sleep(2)

driver.quit()
