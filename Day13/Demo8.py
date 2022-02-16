import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#enter the URL & wait till the page is loaded
driver.get("https://www.actimind.com/")
time.sleep(3)
#if the element is present at the invisible area of the page(bottom) then selenium will do auto scroll
driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").click()
time.sleep(6)