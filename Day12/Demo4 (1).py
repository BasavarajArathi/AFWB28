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
a1=driver.find_element(By.ID,"A1")
v=a1.get_attribute("value")
print(v) #bhanu
a1.send_keys("akshara")
v=a1.get_attribute("value")
print(v)#bhanuakshara

a4=driver.find_element(By.ID,"A4")
v=a4.get_attribute("value")
print(v) #bhanu

# element=driver.find_element(By.ID,"A2")
#
# tag=element.tag_name
# print(tag) #a
#
# id=element.get_attribute("id")
# print(id) #A2
#
# href=element.get_attribute("href")
# print(href)#google.com
#
# text=element.text
# print(text) #Link
#
# time.sleep(1)
