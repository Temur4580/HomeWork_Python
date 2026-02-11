from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()

button = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.ID, "updatingButton")
)
print(button.text)

driver.quit()
