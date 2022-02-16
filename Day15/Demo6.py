import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://news.google.com/")
driver.maximize_window()
time.sleep(2)

for i in range(1,10):
    scroll_bar = driver.find_element(By.XPATH, "//div[@role='navigation']")
    driver.execute_script("arguments[0].scrollBy(0,50)",scroll_bar)
    time.sleep(0.5)


time.sleep(5)
