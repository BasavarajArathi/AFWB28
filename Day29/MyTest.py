import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from day29.loginpage import LoginPage

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
loginpage_obj=LoginPage(driver)
loginpage_obj.set_user_name("admin")
loginpage_obj.set_password("manager")
loginpage_obj.click_login_button()
time.sleep(4)