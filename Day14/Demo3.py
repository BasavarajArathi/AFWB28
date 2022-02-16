import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#scroll to the bottom of the page
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://www.actimind.com/")
#maxmize the window
driver.maximize_window()
time.sleep(1)
js_code="window.scrollTo(0,document.body.scrollHeight)" #java script to scroll the page
print(js_code)
driver.execute_script(js_code) #run the java script
time.sleep(25)
