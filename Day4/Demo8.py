import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.google.com")

# driver.fullscreen_window()
size=driver.get_window_size() # get the current size(h,w) of the browser
print(size)
time.sleep(3)
driver.set_window_size(300,400)

time.sleep(3)
position=driver.get_window_position()#get the current location(x,y) of the browser
print(position)
driver.set_window_position(400,100)
time.sleep(3)
