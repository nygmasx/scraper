from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="./chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://forever-vacation.com/")

email_input = driver.find_element(By.XPATH, "//input[@type='email']")
button = driver.find_element(By.XPATH, "//*[name()='button' or (name()='input' and (@type='submit' or @type='button'))]")
email_input.send_keys("imraneeslk@gmail.com")
email_input.send_keys(Keys.ENTER)
time.sleep(30)

driver.quit()