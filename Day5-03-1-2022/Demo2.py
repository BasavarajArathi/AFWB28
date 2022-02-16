import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#close method closes current browser
#quit method closes all the browser

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.naukri.com")
time.sleep(3)
driver.quit()

time.sleep(60)