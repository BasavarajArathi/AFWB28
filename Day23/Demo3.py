import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
#HANDLING POPUP 2 FILE UPLOAD POPUP
# we cant inspect the file upload popup
# this is used to browse and select the file to be uploaded
#we cant click on Choose file /Browse button
#in selenium to handle file upload, we should use send_keys method with the path of the file to be uploaded
#element should be browser/choose file button
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("file:///F:/B28/PopUpDemo.html")
time.sleep(2)
#click on the choose file button
driver.find_element(By.ID,"A2").send_keys("f:/book1.xlsx")
time.sleep(5)