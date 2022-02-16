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
list_box=driver.find_element(By.ID,"A2")
select=Select(list_box)
all_options=select.options  #return all the options present in listbox
count=len(all_options)
print(count)

for option in all_options:
    print(option.text)

    # for i in range(count):
    #     option1=all_options[i]
    #     print(option1.text)
