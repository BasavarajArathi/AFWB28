import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Handling NOTIFICATION POPUP
#it will be displayed below address bar but at the left side, 2 button Allow & Block
# we cant inspect- so we handle this by changing the browser setting

options=webdriver.ChromeOptions()
options.add_argument("--disable-notifications") #hiding the notification popup

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=options)
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://pushalert.co/demo")
time.sleep(3)
#click send notification button
driver.find_element(By.ID,"send-button").click()
time.sleep(10)