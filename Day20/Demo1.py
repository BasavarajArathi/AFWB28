import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(4)
driver.get("file:///F:/B28/sample1.html")

time.sleep(2)
driver.switch_to.frame(0)  #using index of the frame  --> int
driver.find_element(By.ID,"t2").send_keys("A")
time.sleep(2)
driver.switch_to.default_content() #main web page
driver.find_element(By.ID,"t1").send_keys("A")

time.sleep(2)
driver.switch_to.frame("f1")  #using id of the frame  --> str
driver.find_element(By.ID,"t2").send_keys("B")
time.sleep(2)
driver.switch_to.default_content() #main web page
driver.find_element(By.ID,"t1").send_keys("B")

time.sleep(2)
frame_element=driver.find_element(By.XPATH,"//iframe")
driver.switch_to.frame(frame_element) #using address the frame --> WebElement
driver.find_element(By.ID,"t2").send_keys("C")
time.sleep(2)
driver.switch_to.parent_frame()
driver.find_element(By.ID,"t1").send_keys("C")
time.sleep(2)
