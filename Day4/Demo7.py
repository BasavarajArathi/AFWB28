import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.com")
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.close()