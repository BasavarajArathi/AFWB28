import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#prin the content of the listbox one by one
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(4)
driver.get("file:///F:/B28/ListBox2.html")
list_box=driver.find_element(By.ID,"A3")
select=Select(list_box)
#return the 1st selected option (NOT the 1st option) and if no options are selected then -NSEE
option=select.first_selected_option
print(option.text)
print("-------")

#return all the selected options (NOT the all the options) and if no options are selected then -empty list
all_selected=select.all_selected_options
print(len(all_selected))
for option in all_selected:
    print(option.text)