import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
"""
XPATH- path of the element in HTML tree
 we start xpath with a dot--- root element ( not mandatory)

"""

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(1)
driver.find_element(By.XPATH,"./html/body/a").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/a").click()
time.sleep(2)


