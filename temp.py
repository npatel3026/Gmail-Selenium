from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import os

# Get absolute path of geckodriver.exe in the same folder
driver_path = os.path.join(os.getcwd(), "geckodriver.exe")
service = Service(driver_path)

# Create Firefox driver
driver = webdriver.Firefox(service=service)

# Open Gmail
driver.get("https://mail.google.com/")
driver.maximize_window()
time.sleep(3)

# Check title
expected_title = "Gmail"
actual_title = driver.title
if expected_title in actual_title:
    print("Title Test Passed ")
else:
    print("Title Test Failed ", actual_title)

# Check email input field
try:
    email_field = driver.find_element(By.ID, "identifierId")
    print("Email Field Test Passed ")
except:
    print("Email Field Test Failed ")

# Check Next button
try:
    next_button = driver.find_element(By.ID, "identifierNext")
    print("Next Button Test Passed ")
except:
    print("Next Button Test Failed ")

# Enter test email and click Next
email_field.send_keys("testemail@gmail.com")
next_button.click()
time.sleep(3)

# Check password field appears
try:
    password_field = driver.find_element(By.NAME, "password")
    print("Password Field Appears ")
except:
    print("Password Field NOT Found ")

# Close browser
driver.quit()
