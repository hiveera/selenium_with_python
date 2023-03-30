print("selenium in python")
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.in")
time.sleep(5)
print(driver.current_url)
print(driver.page_source)
driver.quit()

