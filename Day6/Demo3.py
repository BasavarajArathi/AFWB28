import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#tag name, id ,name ,class name,cssSelector,xpath  linktext,plt

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(1)

driver.find_element(By.TAG_NAME,'a').click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.ID,'a1').click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.NAME,'n1').click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.CLASS_NAME,'c1').click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.LINK_TEXT,'aksharatraining').click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,'akshara').click()

time.sleep(10)