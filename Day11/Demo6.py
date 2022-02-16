import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#s1: checkbox is in left side- using xpath
driver.get("file:///F:/B28/Table1.html")
xp="//td[.='Java']/..//input"
driver.find_element(By.XPATH,xp).click()
time.sleep(2)

#s2: checkbox is in right side- using xpath
driver.get("file:///F:/B28/Table2.html")
xp="//td[.='Java']/..//input"
driver.find_element(By.XPATH,xp).click()
time.sleep(2)

#s3: checkbox is in left side- using relative locator
driver.get("file:///F:/B28/Table1.html")
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)
driver.find_element(locate_with(By.TAG_NAME,"input").near(java_element)).click()
time.sleep(2)

#s4: checkbox is in right side- using relative locator
driver.get("file:///F:/B28/Table2.html")
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)
driver.find_element(locate_with(By.TAG_NAME,"input").near(java_element)).click()
time.sleep(2)