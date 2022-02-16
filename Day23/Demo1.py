import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#HANDLING POPUP 1 ALERT POPUP
#we cant inspect alert popup
#it will be displyed below address bar and in the middle
#How do u handle alert popup? ---using switch_to.alert
#what are the options we have under ALert class?
#.text {MSG}     .accept() {OK}      .dismiss(){cancel}
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("file:///F:/B28/PopUpDemo.html")
#click on the submit button
driver.find_element(By.ID,"A1").click()
time.sleep(1)
alert=driver.switch_to.alert
msg=alert.text
print(msg)
alert.accept() #click ok
# alert.dismiss() #click cancel
time.sleep(6)
