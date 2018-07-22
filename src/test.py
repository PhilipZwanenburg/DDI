# Zero-fee ETFs: https://www.scotiabank.com/itrade/en/0,,4200,00.html
# symbols: XCH, XIT, QQC.F

#from lxml import html
#import requests

#if __name__ == "__main__":
#	page = requests.get("https://www.barchart.com/etfs-funds/quotes/XIT.TO/price-history/historical")
#	print(page.content, file=open("tmp.txt", "a"))
#	tree = html.fromstring(page.content)
#
#	print(tree)


# Maybe try this:
# https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python?noredirect=1&lq=1
#
# as it seems that the data is not included in the page source...

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

browser=webdriver.Firefox()
browser.get('https://www.barchart.com/etfs-funds/quotes/XIT.TO/price-history/historical')

soup=BeautifulSoup(browser.page_source,"lxml")
html_content = soup.prettify()
print("Printing output to tmp.txt")
print(html_content, file=open("tmp.txt", "w"))

# Extremely slow
##do something useful
##prints all the links with corresponding text
#for link in soup.find_all('a'):
#    print(link.get('/18',None),link.get_text())
