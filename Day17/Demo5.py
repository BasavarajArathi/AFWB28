import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#login and logout code for actitime application

#most of the time selenium will be faster than app- hence we get NSEE
# match selenium speed with app---synchronization


#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10) #dynamic wait
#goto demo.actitime.com
driver.get("https://demo.actitime.com/login.do")
#enter username
driver.find_element(By.ID,"username").send_keys("admin")
#enter password
driver.find_element(By.NAME,"pwd").send_keys("manager")
#click  on login button
driver.find_element(By.XPATH,"//div[.='Login ']").click()
#click logout
driver.find_element(By.ID,"logoutLink").click()
#close the browser
driver.close()
time.sleep(4)  #blind wait