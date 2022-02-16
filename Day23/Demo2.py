import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
#HANDLING POPUP 1 ALERT POPUP
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
time.sleep(2)
wait=WebDriverWait(driver,5)
try:
    wait.until(expected_conditions.alert_is_present())
    print("alert popup is dispalyed")
    alert=driver.switch_to.alert
    print("MSG:",alert.text)
    alert.accept()
except:
    print("Alert Popup is not Displayed")

time.sleep(5)