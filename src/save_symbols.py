# -*- coding: utf-8 -*-

import argparse
import csv

import urllib.request as urllib2
from bs4 import BeautifulSoup

def get_symbols_itrade (symbols=None):
	"""
	Returns:
	List commission-fee ETF symbols from Scotiabank's iTRADE platform.
	"""

	url = "https://www.scotiabank.com/itrade/en/0,,4200,00.html"

	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page,"lxml")

	table = soup.find('table', {'class': 'table table-striped table-padding'})
	entries = table.find_all('a')
	symbols = [entries[i].contents[0]+".TO" for i in range(len(entries))]
	return symbols

def get_symbols_custom (symbols):
	return symbols

if __name__ == "__main__":
	""" Outputs csv file containing symbols as specified by the input type.
	"""

	parser = argparse.ArgumentParser()
	parser.add_argument('--symbols_type', required=True,\
	                    help="Type of desired symbols. Options: 'itrade', 'custom'.")
	parser.add_argument('--custom_symbols', nargs='+',help="List of custom symbols. e.g.: IYW XSP.TO")
	args = parser.parse_args()


	symbol_functions = {
		"itrade": get_symbols_itrade,
		"custom": get_symbols_custom,
	}

	t = vars(args)["symbols_type"]
	s = vars(args)["custom_symbols"]
	symbols = symbol_functions[t](s)


	with open("../build/symbols_"+t+".csv",'w', newline='') as csvfile:
		w = csv.writer(csvfile)
		w.writerow(["ETF Symbols"])

		w = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
		for s in symbols:
			w.writerow([str(s)])
