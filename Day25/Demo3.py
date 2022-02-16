import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Handling NOTIFICATION POPUP
#it will be displayed below address bar but at the left side, 2 button Allow & Block
# we cant inspect- so we handle this by changing the browser setting

#NOTE: to change the browser setting we use ChromeOptions object
options=webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications":2} #select 'Block'
options.add_experimental_option("prefs",prefs)
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=options)
#maximize the window
driver.maximize_window()
#set the time out
driver.implicitly_wait(4)
#enter the URL
driver.get("https://pushalert.co/demo")
time.sleep(2)
#click send notification button
driver.find_element(By.ID,"send-button").click()
time.sleep(2)
msg=driver.find_element(By.ID,"pa_class-blocked-info").text
print(msg)
time.sleep(3)