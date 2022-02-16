import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://www.istqb.org/")
#find the 'About us' menu
menu=driver.find_element(By.XPATH,"(//a[text()='About us '])[2]")
#move the mouse pointer on the menu (mouse hover)
action=ActionChains(driver)
action.move_to_element(menu).perform()
time.sleep(1)
#click on sub menu
driver.find_element(By.XPATH,"(//a[.='Values '])[2]").click()
time.sleep(6)
