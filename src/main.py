#!/usr/bin/env python3
#
# This file is part of DDI.
#
# DDI is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or
# any later version. DDI is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with DDI. If not, see
# <http://www.gnu.org/licenses/>.
## \file

import sys, os, time
import tensorflow as tf
import numpy as np
import pandas as pd

# Fix for: ImportError: cannot import name 'is_list_like' (https://stackoverflow.com/a/50970152/5983549)
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as pd_dr

import asyncio, aiohttp

from fake_useragent import UserAgent




class Symbol_Scraper:
	def __init__ (self):
		pass

	async def _fetch(self, symbol, url, session):
		""" Retrieve option quotes as JSON
		Params:
		symbol : str(), ETF
		url : str(), request url
		session : aiohttp.ClientSession() object
		Returns:
		response : text object
		"""
		async with session.get(url.format(symbol)) as response:
			return await response.text()

	async def run (self, symbols):
		""" Aggregates response option quotes
		Params:
		symbols : list of str(), ETF symbols
		Returns:
		responses : list of text
		"""
		# url = 'https://www.barchart.com/stocks/quotes/{}/options'
		url = 'https://www.barchart.com/etf-funds/quotes/{}/price-history/historical'

		tasks = []
		async with aiohttp.ClientSession() as session:
			for symbol in symbols:
				task = asyncio.ensure_future(self._fetch(symbol, url, session))
				tasks.append(task)
				# gather returns responses in original order not arrival order
				#   https://docs.python.org/3/library/asyncio-task.html#task-functions
				responses = await asyncio.gather(*tasks)
				return responses


if __name__ == "__main__":
	"""
	\todo Change input to file containing desired etfs for investigation.
	"""
	assert len(sys.argv) == 2,"Insufficient inputs. Need path as first argument"
	src_dir = sys.argv[1]

	# etfs = ["IYW","VXX"]
	etfs = ["IYW"]
	print("\nAsync Barchart Scraper starting.\n")
	print("Retrieving data for the following etfs: ",etfs)

	# GET HTML SOURCE FOR LAST SYMBOL EQUITY PRICE
	loop = asyncio.get_event_loop()

	ss = Symbol_Scraper()
	ss_run_future = asyncio.ensure_future(ss.run(etfs))

	loop.run_until_complete(ss_run_future)
	ss_run = ss_run_future.result()
	# print(ss_run) # HTML for the website.

	# create price dictionary
	ss_dict = {}
	for k, v in zip(etfs, ss_run):
		ss_dict[k] = v

	print(ss_dict) # Still HTML here

	# RUN FIRST ASYNC SCRAPER
	# ua = UserAgent()
	# loop = asyncio.get_event_loop()

	# first_scraper = first_async_scraper()
	# first_run_future = asyncio.ensure_future(first_scraper.run(ETFS, ua.random))

	# loop.run_until_complete(first_run_future)
	# first_run = first_run_future.result()
