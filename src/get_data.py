# -*- coding: utf-8 -*-

import argparse, csv, json, re, time
import pandas as pd
import numpy as np

DATA_DIR = "../build/data/"

def get_input_params (args):
	params_i = {}

	with open(vars(args)["keys_file"]) as f:
		for line in f:
			name, var = line.partition(" ")[::2]
			params_i[name.strip()] = str(var.strip())

	with open(vars(args)["symbols_file"],"r") as f:
		reader = csv.reader(f)
		symbols = list(reader)[1:] # skip the headers
		params_i["symbols"] = [item for sublist in symbols for item in sublist]

	return params_i

def get_time_series (url):
	"""
	Returns
	The time series data in json format if available, None otherwise.
	"""

	possible_key = ["Error Message", "Information", "Time Series (Daily)"]

	df = pd.read_json(url,typ='series')
	json_df = json.loads(df.to_json())

	keys = json_df.keys()
	if (possible_key[0] in keys):
		print("\tGot: "+json_df[possible_key[0]])
		return None
	elif (possible_key[1] in keys):
		if ("if you would like to have a higher API call volume" in json_df[possible_key[1]]):
			print("\tGot: "+json_df[possible_key[1]])
			print("\tSleeping for 65 seconds.")
			time.sleep(65)
			return get_time_series(url)
	elif (possible_key[2] in keys):
		return json.loads(df.to_json())["Time Series (Daily)"]
	else:
		raise ValueError("None of the possible keys ("+str(possible_key)+") were in the json dataframe keys ("+str(keys)+").")

def convert_time_series_data_to_np (data):
	""" Returns the input time series data as a cleaned, sorted numpy array.
	"""

	data_np = np.asarray(data)

	n_col = 6
	n_row = len(data_np)/n_col

	assert n_row.is_integer(),"Invalid data."
	n_row = int(n_row)

	data_np = data_np.reshape(n_row,n_col)
	data_np.sort(axis=0)

	# Clean rows which have 0 volume
	ind_0 = [i if data_np[i][-1] == '0' else None for i in range(len(data_np))]
	ind_0 = [e for e in ind_0 if not e == None]
	data_np = np.delete(data_np,ind_0,0)

	return data_np

def get_data_alpha_vantage (args):
	""" Get financial data from the alpha vantage API.
	"""

	data_names = ['1. open', '2. high', '3. low', '4. close', '5. volume',]
	csv_names = ['date','open', 'high', 'low', 'close', 'volume',]
	p_re = re.compile("\d.\s")

	# Consider making the function flexible in future (TIME_SERIES_INTRADAY).
	url_t = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}"

	params_i = get_input_params(args)
	# print(params_i)

	apikey = params_i["key__alpha_vantage"]
	for symbol in params_i["symbols"]:
		url = url_t.format(symbol,apikey)
		print("Scraping: ",url)

		j_i = get_time_series(url)
		if (j_i == None):
			continue

		keys = list(j_i.keys())

		data = []
		for key in keys:
			if (p_re.match(key)):
				continue
			data += [key]+[j_i[key][name] for name in data_names]

		data_np = convert_time_series_data_to_np(data)

		df = pd.DataFrame(data = data_np, columns = csv_names)
		df.to_csv(DATA_DIR+symbol+".csv")


def get_parsed_args ():
	parser = argparse.ArgumentParser()
	parser.add_argument('--api',          required=True,\
	                    help="The API to be used to obtain the data. Options: 'alpha_vantage'.")
	parser.add_argument('--keys_file',    required=True,help="txt file containing api keys.")
	parser.add_argument('--symbols_file', required=True,help="csv file containing symbol names.")
	parser.add_argument('--api_function',\
	                    help="The API to be used to obtain the data. Options: 'alpha_vantage'.")
	return parser.parse_args()

if __name__ == "__main__":
	""" Collect financial data from specified API and output to csv file.

	Currently supports usage of the following APIs:
	- Alpha Vantage: https://www.alphavantage.co/documentation/
	"""

	args = get_parsed_args()

	get_data = {
		"alpha_vantage": get_data_alpha_vantage,
	}
	get_data[vars(args)["api"]](args)
