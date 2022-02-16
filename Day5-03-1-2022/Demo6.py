import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# element=driver.switch_to.active_element
# element.send_keys("python")

driver.switch_to.active_element.send_keys("python")

time.sleep(15)