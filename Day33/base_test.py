import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#driver---->local variable
#self.driver--->global variable

class BaseTest:

    @pytest.fixture(autouse=True)
    def open_close_app(self):
        #open the browser
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #maximize the browser
        self.driver.maximize_window()

        #implicit wait
        self.driver.implicitly_wait(10)

        #explicit wait
        self.wait=WebDriverWait(self.driver,10)

        #enter the URL
        self.driver.get("http://www.google.com")

        yield #Go,run the test and come back

        #close the browser
        self.driver.close()
