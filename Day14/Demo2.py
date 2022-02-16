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
#maxmize the window
driver.maximize_window()
time.sleep(1)
#find the height of the menu bar
h=driver.find_element(By.XPATH,"/html/body/header").size['height']
#find the vertical distance of the Learn more button
y=driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").location['y']
y=y-h #new scrolling height should avoid menu bar
js_code="window.scrollTo(0," + str(y)+")" #java script to scroll the page
print(js_code)
driver.execute_script(js_code) #run the java script
time.sleep(25)
