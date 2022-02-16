#in Page object Model we create one class for each web page
#Name of the class will be same as respective page name
#Name will be ending with the word 'Page'
#each POM class will have declaration of the element(locator and its value) present on respective poge
#each POM class will have initialization -contructor
#POM class will have getter and setter methods
#POM class is used to store elements and respective methods - Repository Class
from selenium.webdriver.common.by import By


class LoginPage:
    #declaration
     __user_name=(By.ID,"username")
     __password=(By.NAME,"pwd")
     __login_button=(By.XPATH,"//div[.='Login ']")

    #initialization
     def __init__(self,driver):
        self.__driver=driver

    #utilization
     def set_user_name(self,un):
        self.__driver.find_element(*self.__user_name).send_keys(un)

     def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

     def click_login_button(self):
        self.__driver.find_element(*self.__login_button).click()