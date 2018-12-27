from logarithmic_returns import log_return_list
from util import convert_dictionary_to_numpy
from alphavantage import get_time_series_daily_adjusted
from constants import apikey
import pandas

def calculate_risk(tickers):
	data = dict()
	for symbol in tickers:
		data[symbol] = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol=symbol, apikey=apikey))['5. adjusted close']

	logReturnData = dict()
	for symbol in data:
		logReturnData[symbol] = log_return_list(data[symbol])

	data = pandas.DataFrame.from_dict(logReturnData)

	meanValues = [data[ticker].mean() for ticker in data]
	stdValues = [data[ticker].std() for ticker in data]

	# Multiply with 250 to accomodate the trading days
	meanValues = [values*250 for values in meanValues]
	variance = [(values*250)**0.5 for values in stdValues]

	# Calculate covariance and correlation
	# Multiply by 250 to accomodate trading days
	covar = [data[ticker].var() * 250 for ticker in data]
	corel = data.corr()

	return (meanValues, variance, covar, corel)


print(calculate_risk(['PG', 'BEI.DE']))