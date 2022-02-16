import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#how do you change the value if text box is disabled?
#jacascript(DOM) doesnt support linktext,partial link text css, & XPATH
#can we send an input/argument to js?
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")
time.sleep(2)

# driver.find_element(By.ID,"un").send_keys("admin") #Python+Selenium
# driver.execute_script("document.getElementById('un').value='Ravi';")
driver.execute_script("alert(arguments[0])","Akshara")
# driver.execute_script("alert(arguments[0]);alert(arguments[1])","Akshara","bhanu")
time.sleep(5)