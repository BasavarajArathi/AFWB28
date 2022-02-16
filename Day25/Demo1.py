import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Handling NOTIFICATION POPUP
#it will be displayed below address bar but at the left side, 2 button Allow 7 Block

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://pushalert.co/demo")
time.sleep(1)
#click send notification button
driver.find_element(By.ID,"send-button").click()
time.sleep(100)