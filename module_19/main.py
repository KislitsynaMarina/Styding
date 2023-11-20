from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Создание экземпляра браузера (например, Chrome)
driver = webdriver.Firefox()

# Открытие страницы
driver.get('https://www.google.com')

# Поиск элементов на странице и взаимодействие с ними
element = driver.find_element(By.NAME, 'q')
element.send_keys('medical data')
element.send_keys(Keys.RETURN)

# Пауза для ожидания загрузки страницы
time.sleep(5)

# Закрытие браузера
driver.quit()