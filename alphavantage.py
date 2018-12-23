import requests

def get_time_series_daily(symbol, apikey, downloadable, function="TIME_SERIES_DAILY", outputsize="compact"):
	datatype = 'json'
	if downloadable:
		datatype = 'csv'
	payload = {'function': function, 'symbol': symbol, 'outputsize': outputsize, 'apikey': apikey, 'datatype': datatype}
	r = requests.get('https://www.alphavantage.co/query', params=payload)
	return r


print(get_time_series_daily(symbol='MSFT', apikey='PQPNGOENWG0YERJ0', downloadable=False))