import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B28/Demo1.html")

textbox=driver.find_element(By.TAG_NAME,"input")
print(type(textbox))

all_textbox=driver.find_elements(By.TAG_NAME,"input")
print(type(all_textbox))
print(len(all_textbox))  #10    ---> 0,1---9

textbox=all_textbox[0]
print(type(textbox))

for i in range(0,10):
    print(i)
    all_textbox[i].send_keys("bhanu")
    time.sleep(1)

for i in range(0,10):
    print(i)
    textbox=all_textbox[i]
    textbox.clear()
    time.sleep(1)

time.sleep(1)
