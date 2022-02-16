import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#Handling list box (combo box, drop down list , single select listbox)
#list box is created using <select> html tag
#content of the listbox is created using <option> tag

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(4)
driver.get("file:///F:/B28/ListBox1.html")
time.sleep(1)
list_box=driver.find_element(By.ID,"A1")

select=Select(list_box)
# select.select_by_index(1)
# time.sleep(1)
# select.select_by_value("c")
# time.sleep(1)
# select.select_by_value("c")
# time.sleep(1)
# select.select_by_visible_text("Agra")
time.sleep(1)
print(select.is_multiple)

time.sleep(6)