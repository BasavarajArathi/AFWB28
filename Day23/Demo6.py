import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


#open the browser
driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://aksharatraining.com/")
driver.get_screenshot_as_file("selenium_page.png")
time.sleep(2)
pyautogui.screenshot("desktop.png")
