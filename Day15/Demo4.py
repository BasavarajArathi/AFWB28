import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
time.sleep(2)
driver.execute_script("document.getElementById('username').value='admin'")
time.sleep(1)
driver.execute_script("document.getElementsByName('pwd')[0].value='manager'")
time.sleep(1)
login_button=driver.find_element(By.XPATH,"//div[.='Login ']")
driver.execute_script("arguments[0].click()",login_button)
time.sleep(5)