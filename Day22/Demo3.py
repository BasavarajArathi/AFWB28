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
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
#find the element
button=driver.find_element(By.XPATH,"//input[@value='Double Click']")
action=ActionChains(driver)
#double click on the element
action.double_click(button).perform()
time.sleep(5)