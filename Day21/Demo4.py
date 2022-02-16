import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#write a script to select all the options present in multi select list box
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#set the timeout
driver.implicitly_wait(4)
#enter the URL
driver.get("file:///F:/B28/ListBox2.html")
#find the listbox
list_box=driver.find_element(By.ID,"A2")
#create object of Select class
select=Select(list_box)
count=len(select.options)
print(count)
for i in range(count-1,-1,-1):
    select.select_by_index(i)
    time.sleep(1)

for i in range(count-1,-1,-1):
    select.deselect_by_index(i)
    time.sleep(1)


time.sleep(3)