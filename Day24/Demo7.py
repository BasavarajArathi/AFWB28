import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(1)
driver.get("https://demo.actitime.com/login.do")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"actiTIME Inc.").click()
time.sleep(6)
driver.get("https://www.actitime.com/")
time.sleep(15)
driver.close()  #????????

time.sleep(5)


