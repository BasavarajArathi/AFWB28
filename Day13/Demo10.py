import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#if the element is loaded only after scrolling then , in selenium if we try to find it with out scrolling
#we get NoSuchElementException

#in selenium there is no direct method to scroll the page, so we use java scritpt

# How to run javascript in the browser manually?
#--> open dev toolbar (f12) ->goto console tab , type javascript and press enter

# How to run javascript in the browser using selenium?
#--> using driver.execute_script("alert('hi')")

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#enter the URL & wait till the page is loaded
driver.get("https://www.actimind.com/")
time.sleep(3)

#scroll down 5 time
for i in range(1,6):
    print(i)
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(1)

#scroll up 5 time
for i in range(1,6):
    print(i)
    driver.execute_script("window.scrollBy(0,-500)")
    time.sleep(1)

time.sleep(5)