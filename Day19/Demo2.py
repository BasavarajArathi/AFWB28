#can we handle syc of find_element using explicit wait?-->yes
# iw,EW,sleep
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[text()='Login ']").click()

for i in range(100):
    print(i)
    try:
        driver.find_element(By.ID,"logoutLink").click()
        print("Hi")
        break
    except:
        print("Bye")

print("The End")