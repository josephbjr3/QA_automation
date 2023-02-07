from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create a variable for chrome driver's file path
PATH = 'C:\Program Files (x86)\chromedriver.exe'
# tell webdriver which browser to use and where the chromedriver is located
driver = webdriver.Chrome(PATH)

# def test_local_access_login():

# open local access
driver.get('https://169.254.1.1')
# time.sleep(1)

# click "advanced"
driver.find_element(By.ID, 'details-button').click()
# time.sleep(1)

# click "proceed to 169.254.1.1(unsafe)"
driver.find_element(By.ID, 'proceed-link').click()
# time.sleep(2)

# login
local_access_pw = 'admin'
driver.find_element(By.NAME, 'password').send_keys(local_access_pw)
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']").submit()


# time.sleep(10)
driver.quit()
