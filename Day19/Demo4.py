# dif syc options we have in selenium
#implicitly_wait
#WebDriverWait  (Explicit wait)
#time.sleep (blind wait)
#custome wait
#set_page_load_timeout

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

n=4
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_page_load_timeout(n)
try:
    driver.get("https://demo.actitime.com/login.do")
    print("Page is loaded with in "+str(n)+" sec")
except:
    print("Page is not loaded with in "+str(n)+" Sec")

print("The End")