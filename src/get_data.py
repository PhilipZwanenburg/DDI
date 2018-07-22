#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

etfs = ["IYW","XSP.TO"]

url_template="https://www.barchart.com/etfs-funds/quotes/{}/price-history/historical"

driver = webdriver.Firefox()
for etf in etfs:
	url = url_template.format(etf)
	print("\n\n\nETF data for: {}".format(etf))
	print(url)
	print("\n")

	driver.get(url)
	text = driver.find_element_by_tag_name("body").text
	print(text) # Working but very slow and only gets default data (last 3 months).
