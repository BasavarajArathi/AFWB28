import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#HANDLING CONTEXT MENU
#when we right click on any element , it will display list of options---CONTEXT MENU
# right clicking is also called - context click-for this we use context_click() of ActionChains class

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#find the 'Right Click Me'
option=driver.find_element(By.XPATH,"//span[.='right click me']")
action=ActionChains(driver)
#right click (context click) on the 'Right Click Me'
action.context_click(option).perform()
time.sleep(2)
#select 'Copy' option from context menu by clicking
copy=driver.find_element(By.XPATH,"//span[.='Copy']")
#action.move_to_element(copy).perform()
time.sleep(2)
copy.click()

time.sleep(3)