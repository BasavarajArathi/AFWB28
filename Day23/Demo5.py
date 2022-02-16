import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#HANDLING POPUP 3 FILE DOWNLOAD POPUP
#in chrome brower when we click on download linl, file gets downloaded automatically
#but in Firefox browser we get a popup- we cant inspect , we cant automate using selenium
# in such cases we can use 3rd party tool---py auto gui -PyAutoGUI

#open the browser
driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
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
time.sleep(2)
#select 'Save file radio button
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(2)
pyautogui.press('enter')
#click on OK
