import requests

def get_time_series_daily(symbol, apikey, function="TIME_SERIES_DAILY", outputsize="compact"):
	payload = {'function': function, 'symbol': symbol, 'outputsize': outputsize, 'apikey': apikey}
	r = requests.get('https://www.alphavantage.co/query', params=payload)
	return r.json()


print(get_time_series_daily(symbol='MSFT', apikey='PQPNGOENWG0YERJ0'))