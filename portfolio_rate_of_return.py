from simple_returns import simple_return_list, simple_return_mean_percentage
from logarithmic_returns import log_return_list, log_return_mean_percentage
from util import convert_dictionary_to_numpy, normalize_series_to_hundered
from alphavantage import get_time_series_daily_adjusted
from constants import apikey
import pandas
import numpy
import matplotlib.pyplot as plt 

# This scripts calculates the rate of return for a portfolio consisting of four stock
# Takes two arrays, array of ticker indices and array of weights
def getPortfolioRateofReturn(tickers, weights):
	data = dict()
	for symbol in tickers:
		data[symbol] = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol=symbol, apikey=apikey))['5. adjusted close']
	
	# Normalize the values
	normalizedDict = dict()
	for symbol in data:
		normalizedDict[symbol] = normalize_series_to_hundered(data[symbol])

	normalizedData = pandas.DataFrame.from_dict(normalizedDict)
	normalizedData.plot(figsize=(15, 6))
	plt.show()

	# Calculate the simple returns for each
	simpleReturnsDict = dict()
	for symbol in normalizedDict:
		simpleReturnsDict[symbol] = simple_return_list(normalizedDict[symbol])

	simpleReturnsData = pandas.DataFrame.from_dict(simpleReturnsDict)

	weights = numpy.array(weights)
	matrix = numpy.dot(simpleReturnsData, weights)
	annual_returns = simpleReturnsData.mean() * 250
	rateOfReturn = numpy.dot(annual_returns, weights)
	return round(rateOfReturn * 100, 2)
