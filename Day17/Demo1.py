import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#count the number of links present in amazon.com

#Note: In general with find_elements we use -XPATH
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL
driver.get("https://www.amazon.in/")
#find all the links
all_links=driver.find_elements(By.XPATH,"//a")
#count them & print
link_count=len(all_links)
print(link_count)