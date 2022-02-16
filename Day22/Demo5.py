import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#HANDLING DOUBLE CLICK


#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/")
time.sleep(3)
block1=driver.find_element(By.XPATH,"//h1[.='Block 1']")
block3=driver.find_element(By.XPATH,"//h1[.='Block 3']")
action=ActionChains(driver)
action.click_and_hold(block1).move_to_element(block3).pause(3).release().perform() #composit action
time.sleep(4)