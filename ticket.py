from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

path = './chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
service = Service(path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tixcraft.com/ticket/area/23_becloser/14650")

# accept cookies
accept_all_cookies_btn = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, "onetrust-accept-btn-handler"))
accept_all_cookies_btn.click()

# pass 
# click vote price
plants = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "14650_4")))

driver.execute_script("arguments[0].click();", plants)

# into buy vote

# select vote

# Find the <select> element
select_element =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "TicketForm_ticketPrice_02")))

# Create a Select object
select = Select(select_element)
selectLen = len(select.options)
# Select an option by index (0-based)
if selectLen >= 2:
    select.select_by_index(2)
else:
    select.select_by_index(1)

# validate image



print('select----------------------------')
print(len(select.options))
