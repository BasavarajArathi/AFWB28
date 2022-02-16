import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("file:///F:/B28/element.html")
time.sleep(1)
#find the element
element1=driver.find_element(By.ID,'A1')
#clear the value
element1.clear()
time.sleep(1)
#enter the new value
element1.send_keys("akshara")
time.sleep(3)