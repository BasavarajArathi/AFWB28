import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[text()='Login ']").click()

wait=WebDriverWait(driver,8)
locator=(By.ID,"logoutLink")
wait.until(expected_conditions.visibility_of_element_located(locator))

driver.find_element(By.ID,"logoutLink").click()