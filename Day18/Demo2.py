import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions
#login and logout code for actitime application

#most of the time selenium will be faster than app- hence we get NSEE
# match selenium speed with app---synchronization
#implicitly_wait can handle sync of only find_element and find_elements

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10) #wait up to 60s
# 2. enter the url
driver.get("https://demo.actitime.com/login.do")
# 3. enter un
driver.find_element(By.ID,"username").send_keys("admin")
# 4. enter pw
driver.find_element(By.NAME,"pwd").send_keys("manager")
# 5. click on login button
driver.find_element(By.XPATH,"//div[text()='Login ']").click()
#explicit wait
wait.until(expected_conditions.title_contains("Enter"))
# 6. print the title---> actiTIME- Enter Time-Track
actual_title=driver.title
print(actual_title)

driver.find_element(By.ID,"logoutLink").click()
wait.until(expected_conditions.title_contains("Login"))
print(driver.title)