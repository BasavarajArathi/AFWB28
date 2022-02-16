import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get('http://www.google.com')
time.sleep(5)

