import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#set the timeout
driver.implicitly_wait(4)
#enter the URL
driver.get("file:///F:/B28/ListBox1.html")
#find the listbox
list_box=driver.find_element(By.ID,"A1")
#create object of Select class
select=Select(list_box)
all_the_options=select.options
print("ALL THE OPTIONS in SINGLE Select ListBox:")

for option in all_the_options:
    print(option.text)

print("----")

select.select_by_index(1)

print("THE 1ST OPTION SELCTED in SINGLE Select ListBox:")
option=select.first_selected_option
print(option.text)

print("ALL THE OPTION SELCTED in SINGLE Select ListBox:")
all_options=select.all_selected_options
print(len(all_options))
print(option.text)