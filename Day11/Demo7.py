import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#find_element returns 'WebElement' ---WebElement has many functions such as 1.clear 2.send_keys 3. click

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("file:///F:/B28/6Element.html")
#find the element by id 'A1'
webelement=driver.find_element(By.ID,"A1")
time.sleep(1)
webelement.clear()
time.sleep(1)
#enter 'akshara' in that element
webelement.send_keys("akshara")
time.sleep(5)
