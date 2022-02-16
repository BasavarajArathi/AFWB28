import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#HANDLING POPUP 4: HTML Popup (Hidden Division popup)
# we can inspect HTML popup , so we handle it using find_element

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
cwh=driver.current_window_handle
print("current_window_handle:",cwh)
# #set the time out
driver.implicitly_wait(4)
# #enter the URL
driver.get("https://demo.actitime.com/login.do")
# time.sleep(1)
driver.find_element(By.LINK_TEXT,"actiTIME Inc.").click()
time.sleep(2)

cwh=driver.current_window_handle
print("current_window_handle:",cwh)

whs=driver.window_handles
print("window_handles",whs)

time.sleep(2)
driver.switch_to.window(whs[1]) #switch to 2nd tab
time.sleep(2)
driver.close()
time.sleep(6)
