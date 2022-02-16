import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#In Selenium before performing any action (click type select) we need to find the element
#to find the element we use locators
#we have 8 locators - present in By class
# TAG_NAME, ID ,NAME,CLASS_NAME,LINK_TEXT,PARTIAL_LINK_TEXT,CSS_SELECTOR, XPATH
#if the specified locator is not matching then we get NoSuchElementException
#if the specified locator is matching with mulitple elements (duplicate) then find element will return 1st matching element

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(1)

# element=driver.find_element(By.TAG_NAME,"a")
# element.click()

driver.find_element(By.TAG_NAME,'a').click()


time.sleep(10)