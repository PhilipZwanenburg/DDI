# -*- coding: utf-8 -*-

# Splinter docs: https://splinter.readthedocs.io/en/latest/index.html

DEBUG = True

import datetime, re
from splinter import Browser
import numpy as np

if DEBUG:
	import time

def get_month_str (m):
	m_str = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	return m_str[m-1]

def click_xpath (browser,xpath_text):
	browser.find_by_xpath("//*[contains(text(), '{}')]".format(xpath_text)).last.click()
	if DEBUG:
		time.sleep(0)

d = datetime.datetime.today()
items_text = [str(d.year),str(d.year),str(d.year-2),get_month_str(d.month),str(d.day)]
url = "https://www.barchart.com/etfs-funds/quotes/xsp.to/price-history/historical"

# Try to convert this to selenium. Better documentation and possible problem with splinter's wait_time.
browser = Browser()
browser.visit(url)
browser.find_by_name("dateFrom").click()
for text in items_text:
	click_xpath(browser,text)

w_time = 10
print("Waiting ("+str(w_time)+")")
# time.sleep(w_time) # Using time.sleep caused page timeout in some cases.
# Wait for the page to load. Increase value if not loaded. Possibly change to use a check for whether specific elements are visible.
print(browser.is_text_present("Time",w_time)) # Currently waiting much longer than w_time...
print("Done waiting.")
text = browser.find_by_tag("body").text



sep = r"Open High Low Last Change Volume"
try:
	text = text.split(sep,1)[1]
except:
	print("Could not split text")
	print(text)

sep = "Time " + sep
text = text.split(sep,1)[0]
text = re.sub("\+","",text)
text = re.sub("unch","0.0",text)

text_split = list(filter(None,text.split('\n')))

text_array = np.asarray(text_split)
n_col = 7
n_days = len(text_array)/n_col

assert n_days.is_integer(),"Missing data. Aborting"
n_days = int(n_days)

text_array = text_array.reshape(n_days,n_col)
print(text_array)

# Possibly helpful if converting above to selenium.
#
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
