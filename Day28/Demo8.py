import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:

    #declaration & initialization of private variables
    __user_name=(By.ID,"username")
    __password=(By.NAME,"pwd")
    __loginbtn=(By.XPATH,"//div[.='Login ']")

    #utilization of the variables
    def set_username(self,un):
        driver.find_element(*self.__user_name).send_keys(un)

    def set_password(self,pw):
        driver.find_element(*self.__password).send_keys(pw)

    def click_loginbtn(self):
        driver.find_element(*self.__loginbtn).click()


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
login_page=LoginPage()

login_page.set_username("admin")
login_page.set_password("manager")
login_page.click_loginbtn()

time.sleep(4)