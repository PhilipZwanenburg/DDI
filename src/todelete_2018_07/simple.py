# -*- coding: utf-8 -*-

# ONLY WORKS FOR A LIMITED SELECTION OF ETFs...

import time
t0 = time.clock()

import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
import datetime as dt
from copy import copy
import warnings
warnings.filterwarnings('ignore',category=pd.io.pytables.PerformanceWarning)
# ================================================================== #
# datetime management

d = dt.date.today()
# ---------- Days ----------
l10 = d - 10 * BDay()
l21 = d - 21 * BDay()
l63 = d - 63 * BDay()
l252 = d - 252 * BDay()
# ---------- Years ----------
l252_x2 = d - 252 * 2 * BDay()
l252_x3 = d - 252 * 3 * BDay()
l252_x5 = d - 252 * 5 * BDay()
l252_x7 = d - 252 * 7 * BDay()
l252_x10 = d - 252 * 10 * BDay()
l252_x20 = d - 252 * 20 * BDay()
l252_x25 = d - 252 * 25 * BDay()
# ================================================================== #
# filepath management

project_dir = r'/home/pzwan/Desktop/c++/DDI/src/'
price_path = project_dir + r'Stock_Price_Data/'
# ================================================================== #
apikey = "2a21af6c4452f7dc094abb4a4711ae05"
def construct_barChart_url(sym, start_date, freq, api_key=apikey):
    '''Function to construct barchart api url'''

    url = 'http://marketdata.websol.barchart.com/getHistory.csv?' +\
            'key={}&symbol={}&type={}&startDate={}'.format(api_key, sym, freq, start_date)
    return url
# ================================================================== #

# header=3 to skip unnecesary file metadata included by State Street
spy_components = pd.read_excel(project_dir + 'SPY_All_Holdings.xls', header=3)
syms = spy_components.Identifier.dropna()
# syms = syms.drop(syms.index[5:]).sort_values()
syms = syms.drop(syms.index[2:]).sort_values()


# List of available ETFs: https://www.barchart.com/etfs-funds/etfs-by-asset-class?dropdown1=1
df = pd.DataFrame([["IYW"],["GOOG"]], columns=["Identifier"]) # Change this to be read from file.
syms = df.Identifier
print("symbols:\n",syms)

def get_minute_data():
    '''Function to Retrieve <= 3 months of minute data for SP500 components'''

    # This is the required format for datetimes to access the API
    # You could make a function to translate datetime to this format
    start = '20180415000000'
    end = d
    freq = 'minutes'
    prices = {}
    symbol_count = len(syms)
    N = copy(symbol_count)
    try:
        for i, sym in enumerate(syms, start=1):
            api_url = construct_barChart_url(sym, start, freq, api_key=apikey)
            # print(api_url)
            # EXIT
            try:
                csvfile = pd.read_csv(api_url, parse_dates=['timestamp'])
                csvfile.set_index('timestamp', inplace=True)
                prices[sym] = csvfile
            except:
                continue
            N -= 1
            pct_total_left = (N/symbol_count)
            print('{}..[done] | {} of {} symbols collected | percent remaining: {:>.2%}'.format(\
                                                                sym, i, symbol_count, pct_total_left))
    except Exception as e:
        print(e)
    finally:
        pass
    px = pd.Panel.from_dict(prices)
    # convert timestamps to EST
    px.major_axis = px.major_axis.tz_localize('utc').tz_convert('US/Eastern')
    return px

pxx = get_minute_data()
print(pxx)
print(pxx[syms[0]].tail())
print(pxx[syms[1]].tail())

try:
    store = pd.HDFStore(price_path + 'Minute_Symbol_Data.h5')
    store['minute_prices'] = pxx
    store.close()
except Exception as e:
    print(e)
finally:
    pass

# ================================================================== #
# timer looking clean #
secs      = np.round( ( time.clock()  - t0 ), 4 )
time_secs = "{timeSecs} seconds to run".format(timeSecs = secs)
mins      = np.round( ( (  time.clock() ) -  t0 )  / 60, 4 )
time_mins = "| {timeMins} minutes to run".format(timeMins = mins)
hours     = np.round( (  time.clock()  -  t0 )  / 60 / 60, 4 )
time_hrs  = "| {timeHrs} hours to run".format(timeHrs = hours)
print( time_secs, time_mins, time_hrs )
