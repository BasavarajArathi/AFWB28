import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#handling Autosuggestion

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#enter the URL
driver.get("http://www.google.com")
driver.maximize_window()

#type python
# driver.switch_to.active_element.send_keys("pyhton")
driver.find_element(By.NAME,"q").send_keys("python")
time.sleep(1)

#find all the autosuggestions
all_autosuggestions=driver.find_elements(By.XPATH,"//span[contains(text(),'python') or contains(text(),'Python')]")

#count the number of autosuggestions
count=len(all_autosuggestions)
print(count) #10

#print text of all the autosuggestions
for autosuggestion in all_autosuggestions:
    print(autosuggestion.text)


# #select 1st Autosuggestion
# all_autosuggestions[0].click()

#select last Autosuggestion
# all_autosuggestions[-1].click()
all_autosuggestions[count-1].click()

time.sleep(6)