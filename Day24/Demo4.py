import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(1)
driver.get("https://www.fb.com")
time.sleep(1)
driver.switch_to.new_window("window")  #open new browser and switch to it -who is the current
driver.get("https://www.google.com")
time.sleep(1)
driver.close()
# 1.close fb
#2. close google -right ans
#3.close both
#4. close none


time.sleep(5)


