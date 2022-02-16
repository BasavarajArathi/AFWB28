import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
#HANDLING POPUP 3 FILE DOWNLOAD POPUP

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("file:///F:/B28/PopUpDemo.html")
time.sleep(2)
#click on the For download link
driver.find_element(By.ID,"A3").click()
time.sleep(2)
#click downloads
driver.find_element(By.ID,"PageLink_8").click()
time.sleep(2)
#click on nodal_datasheet.pdf
driver.find_element(By.ID,"DirectLink_12").click()
time.sleep(5)
