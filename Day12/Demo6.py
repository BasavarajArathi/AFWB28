import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://demo.actitime.com/login.do")
#find the user name
element=driver.find_element(By.ID,'username')
location=element.location
print(location)
print(location['x'])
print(location['y'])

size=element.size
print(size)
print(size['height'])
print(size['width'])


