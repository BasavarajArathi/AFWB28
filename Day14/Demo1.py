import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#to click on submit button we can use click or submit function
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("file:///F:/B28/element.html?")
time.sleep(1)
# driver.find_element(By.ID,"A7").submit() #this is not a submit button --.NoSuchElementException
# driver.find_element(By.ID,"A8").click()
driver.find_element(By.ID,"A8").submit()
time.sleep(1)
