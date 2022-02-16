import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://news.google.com/")
driver.maximize_window()
time.sleep(2)
health_element=driver.find_element(By.XPATH,"(//span[.='Health'])[1]")
driver.execute_script("arguments[0].scrollIntoView()",health_element)
time.sleep(5)
# for i in range(1,10):
#     driver.execute_script("window.scrollBy(0,500)")
#     time.sleep(1)
#
# for i in range(1,10):
#     driver.execute_script("window.scrollBy(0,-500)")
#     time.sleep(1)