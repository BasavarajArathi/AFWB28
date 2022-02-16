import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")

all_textbox=driver.find_elements(By.TAG_NAME,"input")
for textbox in all_textbox[::-1]:
    textbox.send_keys("bhanu")

for textbox in reversed(all_textbox):
    textbox.clear()

time.sleep(1)