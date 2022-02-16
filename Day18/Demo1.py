import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#login and logout code for actitime application

#most of the time selenium will be faster than app- hence we get NSEE
# match selenium speed with app---synchronization
#implicitly_wait can handle sync of only find_element and find_elements

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(20)
# 2. enter the url
driver.get("https://demo.actitime.com/login.do")
# 3. enter un
driver.find_element(By.ID,"username").send_keys("admin")
# 4. enter pw
driver.find_element(By.NAME,"pwd").send_keys("manager")
# 5. click on login button
driver.find_element(By.XPATH,"//div[text()='Login ']").click()
# 6. print the title---> actiTIME- Enter Time-Track
actual_title=driver.title
print(actual_title)
time.sleep(6)