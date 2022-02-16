import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#can we use mulitple attributes in CSS SELECTOR?---> YES
"""
a[id='a1']---> tag should be a AND id should be a1  ----> a#a1
#a1---> id should be a1  (tag can be anything)

a[class='c1']--->a.c1--> tag should be a AND class should be c1 
.c1---->class should be c1 (tag can be anything)
 

"""

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[id='a1'][name='n1']").click()    #and
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[id='a1'],[name='n1']").click() #or
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a#a1").click()  #  # means id
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#a1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a.c1").click()        # . means class
time.sleep(4)


