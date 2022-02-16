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
time.sleep(2)
unTB=driver.find_element(By.ID,"username")

name=unTB.get_dom_attribute("name")
print(name)

html_code=unTB.get_property("outerHTML")
print(html_code)

#for accessibility testing
print(unTB.accessible_name)

print(unTB.aria_role)

