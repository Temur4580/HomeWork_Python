from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Выполняем задание
driver.get("http://uitestingplayground.com/classattr")
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

# Ждем чтобы увидеть результат
time.sleep(2)

# Закрываем
driver.quit()

print("✅ Задание выполнено!")