import urllib2
from bs4 import BeautifulSoup

page=urllib2.urlopen('http://money.rediff.com/index.html')
soup=BeautifulSoup(page,'html.parser')
BSEBox=soup.find('span',attrs={'id':'bseindex'})
NSEBox=soup.find('span',attrs={'id':'nseindex'})
type_text=soup.find(id="srchword")

#print type_text

print BSEBox.get_text()
print NSEBox.get_text()
