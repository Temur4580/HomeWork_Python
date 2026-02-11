from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

try:
    wait = WebDriverWait(driver, 15)

    # 1. Ждём исчезновения спиннера (индикатора загрузки)
    wait.until(
        EC.invisibility_of_element_located((By.ID, "spinner"))
    )

    # 2. Ждём, пока на странице появится минимум 3 изображения
    #    И у всех них будет заполнен атрибут src
    wait.until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3 and
                  all(img.get_attribute("src") for img in d.find_elements(By.TAG_NAME, "img")[:3])
    )

    # 3. Получаем все изображения
    images = driver.find_elements(By.TAG_NAME, "img")

    # 4. Выводим src третьей картинки
    if len(images) > 2:
        print(images[2].get_attribute("src"))
    else:
        print(f"Найдено только {len(images)} изображений")

finally:
    driver.quit()
