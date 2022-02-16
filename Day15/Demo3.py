import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(2)
#find element using selenium-XPATH
element=driver.find_element(By.XPATH,"//input[@id='un']");

#but change the value using JS (even if element is disabled)
driver.execute_script("arguments[0].value='Ravi'",element)

# driver.execute_script("e=arguments[0];e.value='Ravi'",e1)
time.sleep(3)