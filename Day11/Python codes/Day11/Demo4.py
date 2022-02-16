import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Table1.html")

#get the subject after 'java' (next subject)
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)


cost=driver.find_element(locate_with(By.TAG_NAME,"td").below(java_element)).text
print(cost)

time.sleep(3)