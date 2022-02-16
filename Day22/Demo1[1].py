import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.istqb.org/")
time.sleep(1000)
menu=driver.find_element(By.XPATH,"(//a[text()='About us '])[2]")
action=ActionChains(driver)
action.move_to_element(menu).perform()
driver.find_element(By.XPATH,"").click()
time.sleep(6000)
