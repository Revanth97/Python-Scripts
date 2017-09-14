import urllib2
from bs4 import BeautifulSoup
#import HTMLParser

quote_page='https://www.bloomberg.com/quote/SPX:IND'
page=urllib2.urlopen(quote_page)
soup=BeautifulSoup(page,'html.parser')
name_box=soup.find('h1',attrs={'class':'name'})
name=name_box.text.strip()
price=soup.find('div',attrs={'class':'price'})
print name
print price.text
