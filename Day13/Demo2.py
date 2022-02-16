import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://demo.actitime.com/login.do")
time.sleep(1)
unTB=driver.find_element(By.ID,"username")
unTB.screenshot("username1.png")  #Portable Network Graphics
unTB.send_keys("bhanu")
unTB.screenshot("username2.png")
Image.open("username2.png").show()

time.sleep(1)