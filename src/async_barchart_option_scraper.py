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

# reference: http://www.blackarbs.com/blog/how-to-scrape-and-parse-600-etf-options-in-10-mins-with-python-and-asyncio/5/18/2017
# code: https://gist.github.com/BlackArbsCEO

# Possibly follow pandas_datareader for python related project functionality (build testing/documentation): https://github.com/pydata/pandas-datareader

import os
import sys
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import time
import asyncio
from fake_useragent import UserAgent
'''set path variables'''
project_dir = "/home/pzwan/Desktop/c++/DDI/src/" ###< \todo Make this general
sys.path.append(project_dir)

import async_option_scraper
import option_parser
# ================================================
today = pd.datetime.today().date()
# ================================================
file_start = time.time()
print('\nAsync Barchart Scraper starting...')
# --------------- \\\
# import symbols
FILE = project_dir + 'ETFList.Options.Nasdaq__M.csv'
ALL_ETFS =  pd.read_csv(FILE)['Symbol']
#drop_symbols = ['ADRE', 'AUNZ', 'CGW', ]
#ETFS = [x for x in ALL_ETFS if x not in set(drop_symbols)]
keep_symbols = ['IYW', 'VXX', 'XLF', ]
ETFS = [x for x in ALL_ETFS if x in set(keep_symbols)]
print("ETFs:",ETFS)

# ================================================
# GET HTML SOURCE FOR LAST SYMBOL EQUITY PRICE
# ================================================
t0_price = time.time()
# --------------- \\\
loop = asyncio.get_event_loop()

px_scraper = async_option_scraper.last_price_scraper()
px_run_future = asyncio.ensure_future(px_scraper.run(ETFS))

loop.run_until_complete(px_run_future)
px_run = px_run_future.result()
# ------------- ///
duration_price =  time.time() - t0_price
print('\nprice scraper script run time: ',
    pd.to_timedelta(duration_price, unit='s'))
# ------------- ///
# create price dictionary
px_dict = {}
for k, v in zip(ETFS, px_run):
    px_dict[k] = v

# ================================================
# RUN FIRST ASYNC SCRAPER
# ================================================
t0_first = time.time()
# --------------- \\\
ua = UserAgent()
loop = asyncio.get_event_loop()

first_scraper = async_option_scraper.first_async_scraper()
first_run_future = asyncio.ensure_future(first_scraper.run(ETFS, ua.random))

loop.run_until_complete(first_run_future)
first_run = first_run_future.result()
# ------------- ///
first_duration =  time.time() - t0_first
print('\nfirst async scraper script run time: ',
    pd.to_timedelta(first_duration, unit='s'))

# ================================================
# EXTRACT EXPIRYS FROM FIRST RUN SCRAPER
# ================================================
xp = async_option_scraper.expirys(ETFS, first_run)
expirys = xp.get_expirys()

# ================================================
# SCRAPE AND AGGREGATE ALL SYMBOLS BY EXPIRY
# ================================================
t0_xp = time.time()
# -------------- \\\
# dict key=sym, values=list of json data by expiry
# create helper logic to test if expirys is None before passing
sym_xp_dict = {}
ua = UserAgent()
xp_scraper = async_option_scraper.xp_async_scraper()
for symbol in ETFS:
    print()
    print('-'*50)
    print('scraping: ', symbol)
    if not expirys[symbol]:
        print('symbol ' + symbol + ' missing expirys')
        continue
    try:
        xp_loop = asyncio.get_event_loop()
        xp_future = asyncio.ensure_future(
            xp_scraper.xp_run(symbol, expirys[symbol], ua.random)
            )
        xp_loop.run_until_complete(xp_future)
        sym_xp_dict[symbol] = xp_future.result()
    except Exception as e:
        print(symbol + ' error: ' + e)
# ------------- ///
duration_xp =  time.time() - t0_xp
print('\nall async scraper script run time: ',
    pd.to_timedelta(duration_xp, unit='s'))

# ================================================
# PARSE ALL COLLECTED DATA
# ================================================
t0_agg = time.time()
# -------------- \\\
all_etfs_data = []
for symbol, xp_list in sym_xp_dict.items():
    print()
    print('-'*50)
    print('parsing: ', symbol)
    list_dfs_by_expiry = []
    try:
        for i in range(len(xp_list)):
            try:
                parser = option_parser.option_parser(
                    symbol, xp_list[i])
                call_df = parser.create_call_df()
                put_df = parser.create_put_df()
                concat = pd.concat([call_df, put_df], axis=0)
                concat['underlyingPrice'] = np.repeat(
                    parser.extract_last_price(px_dict[symbol]),
                    len(concat.index))
                list_dfs_by_expiry.append(concat)
            except: continue
    except Exception as e:
        print(f'symbol: {symbol}\n error: {e}')
        print()
        continue
    all_etfs_data.append(pd.concat(list_dfs_by_expiry, axis=0))
# ------------- ///
duration_agg =  time.time() - t0_agg
print('\nagg parse data script run time: ',
    pd.to_timedelta(duration_agg, unit='s'))
# -------------- \\\
dfx = pd.concat(all_etfs_data, axis=0).reset_index(drop=True)
print(dfx.info())
# ------------- ///

# ================================================
# GET ANY MISSING UNDERLYING PRICE
# ================================================
print('\nCollecting missing prices...')
grp = dfx.groupby(['symbol'])['underlyingPrice'].count()
missing_symbol_prices = grp[grp == 0].index

get_price = lambda symbol: web.DataReader(
#    symbol, 'google', today)['Close']  # The google API was deprecated due to being unstable.
    symbol, 'yahoo', today)['Close']
prices = []
for symbol in missing_symbol_prices:
    px = get_price(symbol).iloc[0]
    prices.append((symbol, px))

df_prices = pd.DataFrame(prices).set_index(0)
for symbol in df_prices.index:
    (dfx.loc[dfx['symbol'] == symbol,
         ['underlyingPrice']]) = df_prices.loc[symbol].iloc[0]

dfx['underlyingPrice'] = dfx.underlyingPrice.astype(float)
print('\nmissing prices added')

# ================================================
# store dataframe as hdf
# ================================================
print(dfx.head(20))
print(dfx.info())

file_duration =  time.time() - file_start
print('\nfile script run time: ', pd.to_timedelta(file_duration, unit='s'))

file_ = project_dir + f'/ETF_options_data_{today}.csv'
dfx.to_csv(file_, encoding='utf-8', index=False)

# ================================================
# kill python process after running script
# ================================================
time.sleep(2)
os.kill(os.getpid(), 9)
