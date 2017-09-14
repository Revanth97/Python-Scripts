from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver=webdriver.Chrome()
driver.get("https://www.gmail.com")
emailid=driver.find_element_by_id('identifierId')
inputmail=raw_input("Enter mail id: ")
emailid.send_keys(inputmail)
button=driver.find_element_by_id('identifierNext').click()
time.sleep(2)
password=driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""")
userpass=raw_input("Enter password: ")

password.send_keys(userpass)
driver.find_element_by_id('passwordNext').click()
time.sleep(10)
#for i in xrange(15,0,-1):
#    time.sleep(1)
#    print i
driver.find_element_by_xpath("""//*[@id=":j6"]/div/div""").click()
receiver=driver.find_element_by_id(""":p6""")
inputreceiver=raw_input("Enter receivers mail id: ")
inputreceiver=inputreceiver+" "
receiver.send_keys(inputreceiver)
textbox=driver.find_element_by_id(""":pq""")
usertext=raw_input("Enter your text to send: ")
textbox.send_keys(usertext)
driver.find_element_by_id(""":of""").click()

