from alphavantage import get_time_series_daily_adjusted
from logarithmic_returns import log_return_list
from util import convert_dictionary_to_numpy, normalize_series_to_hundered
from constants import apikey
import pandas
import numpy
import matplotlib.pyplot as plt 
import random

def getEfficientFrontier(tickers):
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

	# Calculate the log returns for each
	logReturnsDict = dict()
	for symbol in normalizedDict:
		logReturnsDict[symbol] = log_return_list(normalizedDict[symbol])

	logReturnsData = pandas.DataFrame.from_dict(logReturnsDict)

	dataMean = logReturnsData.mean() * 250
	dataCov = logReturnsData.cov() * 250
	dataCor = logReturnsData.corr()

	pf_returns = []
	pf_vols = []
	num_assets = len(tickers)

	for x in range(1000):
		weights = numpy.random.random(num_assets)
		weights /= numpy.sum(weights)
		# Expected portfolio return
		pf_returns.append(numpy.sum(weights * dataMean) * 250)
		pf_vols.append((numpy.dot(weights.T, numpy.dot(dataCov, weights))) ** 0.5)

	pf_returns = numpy.array(pf_returns)
	pf_vols = numpy.array(pf_vols)

	portfolios = pandas.DataFrame({'Returns': pf_returns, 'Volatility': pf_vols})
	portfolios.plot(x='Volatility', y='Returns', kind='scatter', figsize=(10,6))
	plt.xlabel('Expected Volatility')
	plt.ylabel('Expected Return')
	plt.show()


getEfficientFrontier(['PG', '^GSPC'])