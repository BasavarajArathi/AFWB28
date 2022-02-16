import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print(driver.window_handles)
driver.get("http://www.google.com")
time.sleep(3)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print(driver.window_handles)
time.sleep(3)
driver.get("http://www.fb.com")
time.sleep(2)
driver.close()
time.sleep(2)