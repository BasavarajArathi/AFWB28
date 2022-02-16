import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(2)
# driver.find_element(By.ID,"un").send_keys("admin") #Python+Selenium
driver.execute_script("document.getElementById('un').value='Ravi';")
time.sleep(5)