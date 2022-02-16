import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Table1.html")
#select the 'java checkbox'
xp="//td[.='Java']/../td[1]/input"
driver.find_element(By.XPATH,xp).click()
time.sleep(3)