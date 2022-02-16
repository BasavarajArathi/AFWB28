import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
#selenium 3 ---JSON (Java Script Object notation) WIRE PROTOCOL
#Selenium4 ---- W3C(WWWC) PROTOCOL

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Table1.html")

#get the subject present before 'API' (previous subject)

xp="//td[.='API']"
api_element=driver.find_element(By.XPATH,xp)

sub=driver.find_element(locate_with(By.TAG_NAME,"td").above(api_element)).text
print(sub)

time.sleep(3)