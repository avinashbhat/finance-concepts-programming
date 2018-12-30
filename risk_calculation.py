from logarithmic_returns import log_return_list
from util import convert_dictionary_to_numpy
from alphavantage import get_time_series_daily_adjusted
from constants import apikey
import pandas
import numpy

def calculate_risk_util(tickers):
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

	return (data, meanValues, variance, covar, corel)


def calculate_portfolio_variance_volatility(tickers, weights):
	weights = numpy.array(weights)
	data, meanVal, variance, covar, corel = calculate_risk_util(tickers)
	portfolio_var = numpy.dot(weights.T, numpy.dot(data.cov() * 250, weights))
	portfolio_vol = portfolio_var ** 0.5
	return (portfolio_var, round(portfolio_vol*100, 2))

def get_diverse_ndiverse_risk(tickers, weights):
	weights = numpy.array(weights)
	data, meanVal, variance, covar, corel = calculate_risk_util(tickers)
	p_var, p_vol = calculate_portfolio_variance_volatility(tickers, weights)
	weightedAnnualVariances = 0
	for index, value in enumerate(covar):
		weightedAnnualVariances += (weights[index] ** 2)*value
	diverse = p_var - weightedAnnualVariances
	nonDiverse = p_var - diverse
	return (round(diverse*100, 2), round(nonDiverse*100, 2))