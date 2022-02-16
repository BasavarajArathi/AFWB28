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
driver.get("file:///F:/B28/ListBox1.html")
time.sleep(1)
list_box=driver.find_element(By.ID,"A1")
text=driver.find_element(By.XPATH,"//option[@value='d']").text
select=Select(list_box)
select.select_by_visible_text(text)
time.sleep(6)