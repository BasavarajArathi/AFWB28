import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL
driver.get("https://demo.actitime.com/login.do")
#enter user name as Admin
driver.find_element(By.ID, "username").send_keys("admin")
#enter pasword as manager
driver.find_element(By.NAME, "pwd").send_keys("manager")
#select the check box
driver.find_element(By.ID, "keepLoggedInCheckBox").click()
#click on Login Button
driver.find_element(By.XPATH, "//div[.='Login ']").click()
time.sleep(5)