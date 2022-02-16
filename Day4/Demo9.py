import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver1=webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
print(driver1.window_handles)
driver1.get("http://www.google.com")
time.sleep(3)

driver2=webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
print(driver2.window_handles)
time.sleep(3)
driver2.get("http://www.fb.com")
time.sleep(2)

driver2.close()
time.sleep(2)
driver1.close()