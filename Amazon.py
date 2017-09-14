# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from datetime import datetime
import time
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.amazon.in")

search=driver.find_element_by_id("twotabsearchtextbox")
usersearch=raw_input("Enter product name: ")
search.send_keys(usersearch,Keys.RETURN)

time.sleep(2)

list_items=driver.find_elements_by_class_name("s-access-title")
list_prices=driver.find_elements_by_css_selector('.a-size-base.a-color-price.s-price.a-text-bold')

items=[]
prices=[]

for item in list_items:
    items.append(item.text)
    print item.text
    print len(items)

for item in list_prices:
    text=item.text
    text=text[1:]
    prices.append(text)
    print item.text
    print len(prices)

table=pd.DataFrame({
    'Product Name':items,
    'Price':prices
    })

table=table[['Product Name','Price']]

print table

filename='products.csv'
#df=pd.DataFrame(table)
table.to_csv(filename,index=False,encoding='utf-8')
