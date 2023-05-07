from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

path = './chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
service = Service(path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tixcraft.com/")