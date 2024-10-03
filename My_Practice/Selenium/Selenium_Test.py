import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://www.zewa.net/ro/")

# Wait for the element to be present
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
driver.maximize_window()
# Locate the element by its ID
input_element = driver.find_element(By.ID, "onetrust-accept-btn-handler")

# Click the element
input_element.click()

time.sleep(8888888)
driver.quit()
