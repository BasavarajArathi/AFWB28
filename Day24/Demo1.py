import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#HANDLING POPUP 4: HTML Popup (Hidden Division popup)
# we can inspect HTML popup , so we handle it using find_element

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://www.flipkart.com/")
time.sleep(1)
#enter username in HTML poppup
driver.switch_to.active_element.send_keys("bhanu")
time.sleep(1)
#enter password in HTML poppup
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("akshara")
time.sleep(1)
#click close button on the HTML popup
driver.find_element(By.XPATH,"//button[text()='✕']").click()
time.sleep(10)
