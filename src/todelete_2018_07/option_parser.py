import pandas as pd
import numpy as np
import re

# ================================================
class option_parser:
    def __init__(self, symbol, response):
        self.symbol = symbol
        self.response = response
    # ------------------------------------------------
    # extract last price from html
    def extract_last_price(self, html_text):
        """fn: extract price from html"""
        reg_exp = r'(?<="lastPrice":)(\d{1,3}.{1}\d{2})'
        prices = re.findall(reg_exp, html_text)
        if len(prices) < 1:
            return np.nan
        else:
            return float(prices[0])
    # ------------------------------------------------
    # create call df
    def create_call_df(self):
        """fn: to create call df"""
        json_calls = self.response['data']['Call']
        list_dfs = []
        for quote in json_calls:
            list_dfs.append(pd.DataFrame.from_dict(quote['raw'], orient='index'))
        df = (
            pd.concat(list_dfs, axis=1).T.reset_index(drop=True)
            .replace('NA', np.nan)
            .apply(pd.to_numeric, errors='ignore')
            .assign(expirationDate = lambda x: pd.to_datetime(x['expirationDate']))
        )
        df['symbol'] = [self.symbol] * len(df.index)
        return df
    # ------------------------------------------------
    # create put df
    def create_put_df(self):
        """fn: to create put df"""
        json_puts = self.response['data']['Put']
        list_dfs = []
        for quote in json_puts:
            list_dfs.append(pd.DataFrame.from_dict(quote['raw'], orient='index'))
        df = (
            pd.concat(list_dfs, axis=1).T.reset_index(drop=True)
            .replace('NA', np.nan)
            .apply(pd.to_numeric, errors='ignore')
            .assign(expirationDate = lambda x: pd.to_datetime(x['expirationDate']))
        )
        df['symbol'] = [self.symbol] * len(df.index)
        return df
