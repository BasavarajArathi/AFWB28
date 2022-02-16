import time
from selenium import webdriver


where_to_run="http://localhost:4444/wd/hub"
which_browser_to_open=webdriver.FirefoxOptions()

driver=webdriver.Remote(command_executor=where_to_run,options=which_browser_to_open)
driver.get("http://www.google.com")
print(driver.title)
time.sleep(2)
driver.close()
