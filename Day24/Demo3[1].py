import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# #set the time out
driver.implicitly_wait(4)

# #enter the URL
driver.get("https://www.naukri.com")

#open new window and goto google.com
driver.switch_to.new_window("window")
driver.get("https://www.google.com")

#open new window and goto google.com
driver.switch_to.new_window("window")
driver.get("https://www.fb.com")

#close all the browsers without using quit
all_window_handles=driver.window_handles
print(len(all_window_handles))
time.sleep(1)

for window_handle in reversed(all_window_handles):
    print(window_handle)
    driver.switch_to.window(window_handle)
    print(driver.title)
    time.sleep(1)
    driver.close()

#
# for window_handle in reversed(all_window_handles):
#     driver.switch_to.window(window_handle)
#     driver.close()
#     time.sleep(1)



time.sleep(8)


