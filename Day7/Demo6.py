import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
"""
XPATH- path of the element in HTML tree
 we start xpath with a dot--- root element ( not mandatory)
 / (forward slash) represents child element
xpath supports index - starts from 1

"""

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo3.html")
driver.find_element(By.XPATH,"/html/body/input").send_keys("A")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/input[1]").send_keys("B")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/input[2]").send_keys("C")
time.sleep(3)