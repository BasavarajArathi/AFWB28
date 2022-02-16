import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Table1.html")

#get the cost of 'java'
xp="//td[.='JAVA']"
java_element=driver.find_element(By.XPATH,xp)


cost=driver.find_element(locate_with(By.TAG_NAME,"td").to_right_of(java_element)).text
print(cost)

time.sleep(3)