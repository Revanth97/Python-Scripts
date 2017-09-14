from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")

mailid=driver.find_element_by_id("email")
usermail=raw_input("Enter mail id: ")


password=driver.find_element_by_id("pass")
userpassword=raw_input("Enter password: ")

mailid.send_keys(usermail)
password.send_keys(userpassword,Keys.RETURN)
