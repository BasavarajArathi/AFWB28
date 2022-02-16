import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#print the text of all the links present on google.com

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#enter the URL
driver.get("http://www.google.com")

#find all the links
all_links=driver.find_elements(By.XPATH,"//a")
link=all_links[0]
link_text=link.text
print(link_text)
