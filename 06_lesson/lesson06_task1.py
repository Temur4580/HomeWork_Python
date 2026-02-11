from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    driver.find_element(By.ID, "ajaxButton").click()

    # Ожидаем появление текста и сразу выводим
    wait = WebDriverWait(driver, 20)
    message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print(message.text)

finally:
    driver.quit()