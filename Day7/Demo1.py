import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#tag name,id ,name,class name,linktext,partial link text,cssSeclector,xpath
#CSS-Cascading Style Sheets
#CSS_SELECTOR-----> tag[AN='AV']
#How to verify CSS_SELECTOR in browser
#inspect any element (F12) ->in dev toolbar -> ctrl + F->type css expression it i will highlight the matching element
#CSS SELECTOR DO NOT SUPPORT TEXT (we cant use text in CSS SELECTOR)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[name='n1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[class='c1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[title='visit page'] ").click()
time.sleep(1)
driver.back()
time.sleep(1)
v="a[href='https://aksharatraining.com/']"
driver.find_element(By.CSS_SELECTOR,v).click()
time.sleep(3)