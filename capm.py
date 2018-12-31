from alphavantage import get_time_series_daily_adjusted
from logarithmic_returns import log_return_list
from util import convert_dictionary_to_numpy, normalize_series_to_hundered
from constants import apikey
import pandas
import numpy
import matplotlib.pyplot as plt 

def calculate_beta(tickers):
	data = dict()
	for symbol in tickers:
		data[symbol] = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol=symbol, apikey=apikey))['5. adjusted close']


	data = pandas.DataFrame.from_dict(data)

	# Calculate the log returns for each
	logReturnsDict = dict()
	for symbol in data:
		logReturnsDict[symbol] = log_return_list(data[symbol])

	logReturnsData = pandas.DataFrame.from_dict(logReturnsDict)

	dataCov = logReturnsData.cov() * 250
	cov_with_market = dataCov.iloc[0,1]

	variance = [logReturnsData[ticker].var() * 250 for ticker in tickers]
	beta = cov_with_market/variance[1]
	return beta