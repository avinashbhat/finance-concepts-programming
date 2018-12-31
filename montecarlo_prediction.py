from simple_returns import simple_return_list, simple_return_mean_percentage
from logarithmic_returns import log_return_list, log_return_mean_percentage
from util import convert_dictionary_to_numpy, normalize_series_to_hundered
from alphavantage import get_time_series_daily_adjusted
from constants import apikey
import pandas
import numpy
import matplotlib.pyplot as plt 
from scipy.stats import norm

def forecasting_stock(tickers):
	data = dict()
	for symbol in tickers:
		data[symbol] = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol=symbol, apikey=apikey))['5. adjusted close']

	logReturnData = dict()
	for symbol in data:
		logReturnData[symbol] = log_return_list(data[symbol])
	
	data = pandas.DataFrame.from_dict(logReturnData)
	data.plot(figsize=(10, 6))
	plt.show()

	dataMean = data.mean()
	dataVar = data.var()
	dataStd = data.std()

	drift = dataMean - (0.5 * dataVar)
	
	t_intervals = 1000
	iterations = 10

	daily_returns = numpy.exp(drift.values + dataStd.values * norm.ppf(numpy.random.rand(t_intervals, iterations)))

	# Predictions 
	S0 = data.iloc[-1]

	price_list = numpy.zeros_like(daily_returns)
	price_list[0] = S0
	for t in range(1, t_intervals):
		price_list[t] = price_list[t-1]*daily_returns[t]
	plt.figure(figsize=(10, 6))
	plt.plot(price_list)
	plt.show()

forecasting_stock(['MSFT'])