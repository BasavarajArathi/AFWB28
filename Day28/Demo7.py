import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:

    user_name=[By.ID,"username"]

    def set_username(self):
        driver.find_element(self.user_name[0],self.user_name[1]).send_keys("admin")

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
login_page=LoginPage()
login_page.set_username()

time.sleep(4)