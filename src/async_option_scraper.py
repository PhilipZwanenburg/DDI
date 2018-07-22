import asyncio
import aiohttp

# ================================================
# for first run only
class first_async_scraper:
    def __init__(self):
        pass

    async def _fetch(self, symbol, url, session, headers):
        """fn: to retrieve option quotes as JSON
        Params:
            symbol : str(), ETF
            url : str(), request url
            session : aiohttp.ClientSession() object
            headers : dict() containing header info
        Returns:
            response : JSON/Python Dict
        """
        async with session.post(url.format(symbol), headers=headers) as response:
            return await response.json(content_type=None)

    async def run(self, symbols, user_agent):
        """fn: to aggregate response option quotes
        Params:
            symbols : list of str(), ETF symbols
            user_agent : str()
        Returns:
            responses : list of JSON
        """
#        url = 'https://core-api.barchart.com/v1/options/chain?symbol=IYW&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CsymbolCode%2CsymbolType&groupBy=optionType&raw=1&meta=field.shortName%2Cfield.type%2Cfield.description'
        url = 'https://core-api.barchart.com/v1/options/chain?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CsymbolCode%2CsymbolType&groupBy=optionType&raw=1&meta=field.shortName%2Cfield.type%2Cfield.description'

        headers = {
                "Accept":"application/json",
                "Accept-Encoding":"gzip, deflate, sdch, br",
                "Accept-Language":"en-US,en;q = 0.8",
                "Connection":"keep-alive",
                "Host":"core-api.barchart.com",
                "Origin":"https://www.barchart.com",
                "Referer":"https://www.barchart.com/etfs-funds/quotes/{}/options",
                "User-Agent":user_agent,
                }

        tasks = []
        async with aiohttp.ClientSession() as session:
            for symbol in symbols:
                headers['Referer'] = headers['Referer'].format(symbol)
                task = asyncio.ensure_future(self._fetch(symbol, url, session, headers))
                tasks.append(task)
            # gather returns responses in original order not arrival order
            #   https://docs.python.org/3/library/asyncio-task.html#task-functions
            responses = await asyncio.gather(*tasks)
            return responses

# ================================================
class expirys:
    def __init__(self, ETFS, first_future_result):
        """Class to extract expiration data from Dict
        Params:
            ETFS : list of ETF symbol str()
            first_future_result : list of response objects (dict/JSON) from the first scraper
        """
        self.ETFS = ETFS
        self.first_future_result = first_future_result

    def _get_dict_expiry(self, response):
        """fn: to get expirations from response dict
        Params:
            response : dict/JSON object
        Returns:
            list() of date str(), "YYYY-MM-DD"
        """
        if response['count'] == 0:
            return None
        else:
            return response['meta']['expirations']

    def get_expirys(self):
        """fn: to create dict with k, v = symbol, list of expirys
                we have to do this b/c JSON/dict response data doesn't
                contain symbol identifier
        Returns:
            dict(symbol = list of expiry dates)
        """
        from itertools import zip_longest
        expirys = {}
        for symbol, resp in zip_longest(self.ETFS, self.first_future_result):
            # we can do this because results are in order of submission not arrival
            #   gather returns responses in original order not arrival order
            #       https://docs.python.org/3/library/asyncio-task.html#task-functions
            expirys[symbol] = self._get_dict_expiry(resp)
        return expirys

# ================================================
# async by url + expirations
class xp_async_scraper:
    def __init__(self):
        pass

    async def _xp_fetch(self, symbol, expiry, url, session, headers):
        """fn: to retrieve option quotes as JSON
        Params:
            symbol : str(), ETF
            expiry : str(), "YYYY-MM-DD"
            url : str(), request url
            session : aiohttp.ClientSession() object
            headers : dict() containing header info
        Returns:
            response : JSON/Python Dict
        """
        async with session.post(url.format(symbol, expiry), headers=headers) as response:
            return await response.json(content_type=None)

    async def xp_run(self, symbol, expirys, user_agent):
        """fn: to aggregate response option quotes
        Params:
            symbol : str(), ETF
            expirys : list of date str() "YYYY-MM-DD"
            user_agent : str()
        Returns:
            responses : list of JSON
        """
        url = "https://core-api.barchart.com/v1/options/chain?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate={}&raw=1&meta=field.shortName%2Cfield.type%2Cfield.description"

        headers = {
                "Accept":"application/json",
                "Accept-Encoding":"gzip, deflate, sdch, br",
                "Accept-Language":"en-US,en;q=0.8",
                "Connection":"keep-alive",
                "Host":"core-api.barchart.com",
                "Origin":"https://www.barchart.com",
                "Referer":"https://www.barchart.com/etfs-funds/quotes/{}/options",
                "User-Agent":user_agent,
                }

        tasks = []
        async with aiohttp.ClientSession() as session:
            for expiry in expirys:
                headers['Referer'] = headers['Referer'].format(symbol)
                task = asyncio.ensure_future(self._xp_fetch(symbol, expiry, url, session, headers))
                tasks.append(task)
            # gather returns responses in original order not arrival order
            #   https://docs.python.org/3/library/asyncio-task.html#task-functions
            responses = await asyncio.gather(*tasks)
            return responses

# ================================================
# async get html page source
class last_price_scraper:
    def __init__(self):
        pass

    async def _fetch(self, symbol, url, session):
        """fn: to retrieve option quotes as JSON
        Params:
            symbol : str(), ETF
            url : str(), request url
            session : aiohttp.ClientSession() object
        Returns:
            response : text object
        """
        async with session.get(url.format(symbol)) as response:
            return await response.text()

    async def run(self, symbols):
        """fn: to aggregate response option quotes
        Params:
            symbols : list of str(), ETF symbols
        Returns:
            responses : list of text
        """
        url = 'https://www.barchart.com/stocks/quotes/{}/options'

        tasks = []
        async with aiohttp.ClientSession() as session:
            for symbol in symbols:
                task = asyncio.ensure_future(self._fetch(symbol, url, session))
                tasks.append(task)
            # gather returns responses in original order not arrival order
            #   https://docs.python.org/3/library/asyncio-task.html#task-functions
            responses = await asyncio.gather(*tasks)
            return responses
