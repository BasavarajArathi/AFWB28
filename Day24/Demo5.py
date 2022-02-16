import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(1)
driver.get("https://demo.actitime.com/login.do")
time.sleep(2)
driver.switch_to.new_window("tab") #open new tab and switch to new tab
time.sleep(1)
driver.get("https://www.actitime.com/")
time.sleep(3)
driver.close()
# 1.close demo
#2. close both
#3.close actitime
#4. close none


time.sleep(5)


