import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Login to actitime app
# 1. open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 2.enter the url
driver.get("https://demo.actitime.com/login.do")
# 3.enter the username as admin
driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("admin")
# 4.enter the password as manager
driver.find_element(By.CSS_SELECTOR,"input[name='pwd']").send_keys("manager")
#5 Select the check box
driver.find_element(By.CSS_SELECTOR,"#keepLoggedInCheckBox").click()
time.sleep(1)
# 6. click on login button
driver.find_element(By.CSS_SELECTOR,"a[id='loginButton']").click()
time.sleep(5)