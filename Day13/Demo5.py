import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#using selenium we cant take screenshot of Desktop
#using selenium we cant take screenshot of complete page (only visible area ., it will not scroll down)

#this code is to take screenshot of a webpage section
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://www.actitime.com/")
time.sleep(1)
driver.get_screenshot_as_file("actitime.png")
