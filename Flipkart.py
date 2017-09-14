# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from datetime import datetime
import time
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com")

search=driver.find_element_by_class_name("LM6RPg")
user_search=raw_input("Enter product to search: ")
search.send_keys(user_search,Keys.RETURN)

time.sleep(2)

list_items=driver.find_elements_by_class_name("_3wU53n")
list_prices=driver.find_elements_by_class_name("_1vC4OE")

items=[]
prices=[]


for item in list_items:
    items.append(item.text)
    #print (item.text)

for item in list_prices:
    text=item.text
    text=text[1:]
    prices.append(text)
    #print text

table=pd.DataFrame({
    'Product Name':items,
    'Price':prices
    })

table=table[['Product Name','Price']]

print table

filename='products.csv'
#df=pd.DataFrame(table)
table.to_csv(filename,index=False,encoding='utf-8')
