
.PHONY: save_symbols_itrade
save_symbols_itrade:
	cd src && python3 save_symbols.py --symbols_type itrade

.PHONY: get_data_itrade
get_data_itrade: save_symbols_itrade
	cd src && python3 get_data.py \
	--api alpha_vantage \
	--symbols_file ../build/symbols_itrade.csv \
	--keys_file ../input/keys/api_keys.txt
