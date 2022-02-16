import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#Handling list box (combo box, drop down list , single select listbox)
#list box is created using <select> html tag
#content of the listbox is created using <option> tag
#to Handle listbox we use Select class of selenium

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(4)
driver.get("file:///F:/B28/ListBox2.html")
time.sleep(1)
list_box=driver.find_element(By.ID,"A2")
select=Select(list_box)

select.select_by_index(0)
time.sleep(1)
select.deselect_by_index(0)
time.sleep(1)
select.select_by_value("b")
time.sleep(1)
select.deselect_by_value("b")
time.sleep(1)
select.select_by_visible_text("Snacks")
time.sleep(1)
select.deselect_by_visible_text("Snacks")
time.sleep(1)
select.deselect_all()


time.sleep(3)
print(select.is_multiple)
time.sleep(6)