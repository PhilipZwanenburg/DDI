# -*- coding: utf-8 -*-

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# etfs = ["IYW","XSP.TO"]

# url_template="https://www.barchart.com/etfs-funds/quotes/{}/price-history/historical"

# driver = webdriver.Firefox()
# for etf in etfs:
# 	url = url_template.format(etf)
# 	print("\n\n\nETF data for: {}".format(etf))
# 	print(url)
# 	print("\n")

# 	driver.get(url)
# 	text = driver.find_element_by_tag_name("body").text
# 	print(text) # Working but very slow and only gets default data (last 3 months).



# Make apikey private
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=cbo.to&apikey=6CRWG9U15LX42NA1

import urllib.request as urllib2
from bs4 import BeautifulSoup

# Zero-fee ETFs from Scotiabank's Itrade platform.
url = "https://www.scotiabank.com/itrade/en/0,,4200,00.html"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page,"lxml")

table = soup.find('table', {'class': 'table table-striped table-padding'})
lines = table.find_all('a')
symbols = [lines[i].contents[0] for i in range(len(lines))]
print(symbols)
