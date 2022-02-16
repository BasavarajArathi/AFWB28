import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

#Handling Notification popup in Firefox browser

ff_options=webdriver.FirefoxOptions()
ff_options.set_preference("permissions.default.desktop-notification",2) # 2--> block notification

#open the firefox browser with above settings
driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=ff_options)
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
#HTML POPUP
msg=driver.find_element(By.ID,"pa_class-blocked-info").text
print(msg)
# time.sleep(3)