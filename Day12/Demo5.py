import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://demo.actitime.com/login.do")
#click on login button (without UN & pwd)
driver.find_element(By.XPATH,"//div[.='Login ']").click()
time.sleep(5)
element=driver.find_element(By.XPATH,"//span[contains(.,'invalid')]")
c=element.value_of_css_property("color")
print("color in RGB format",c)
h=Color.from_string(c).hex
print("Color in Hex Format",h)

font_size=element.value_of_css_property("font-size")
print("Font Size:",font_size)

font_name=element.value_of_css_property("font-family")
print("Font Name:",font_name)
