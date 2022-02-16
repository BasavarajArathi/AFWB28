# dif syc options we have in selenium
#implicitly_wait---------------------find_element & find_elements
#WebDriverWait  (Explicit wait)------- any function
#set_page_load_timeout----------get()
#set_script_timeout------execute_script()
#time.sleep (blind wait)---> any
#custome wait--->any

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

n=4
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_page_load_timeout(n)
driver.set_script_timeout(n)
try:
    driver.get("https://demo.actitime.com/login.do")
    print("Page is loaded with in "+str(n)+" sec")
except:
    print("Page is not loaded with in "+str(n)+" Sec")

# driver.execute_script("alert('hi')")
#1. send js code to browser (script injuction)
#2. send the request to browser to run the javascript
#3. wait till the execution of java script (wait till it gets response from browser)
#4. goto next step

print("The End")