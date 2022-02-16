import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element(By.XPATH,"(//button)[2]").click()
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("iphone")
time.sleep(2)
all_phone=driver.find_elements(By.XPATH,"//span[text()='iphone']/../..")

for phone in all_phone:
    print(phone.text)
time.sleep(1)

all_phone[0].click()

time.sleep(30)