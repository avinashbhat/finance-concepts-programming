import requests
from util import convert_dictionary_to_numpy

def get_time_series_daily(symbol, apikey, function="TIME_SERIES_DAILY", outputsize="compact"):
	payload = {'function': function, 'symbol': symbol, 'outputsize': outputsize, 'apikey': apikey}
	r = requests.get('https://www.alphavantage.co/query', params=payload)
	return r.json()['Time Series (Daily)']

def get_time_series_daily_adjusted(symbol, apikey, function="TIME_SERIES_DAILY_ADJUSTED", outputsize="full"):
	payload = {'function': function, 'symbol': symbol, 'outputsize': outputsize, 'apikey': apikey}
	r = requests.get('https://www.alphavantage.co/query', params=payload)
	return r.json()['Time Series (Daily)']
