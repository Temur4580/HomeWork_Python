# lesson05_task2.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

time.sleep(2)
driver.quit()