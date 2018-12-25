from matplotlib import pyplot as plt
import math


def simple_return(stock):
	stock['simpleReturn'] = [(float(value)/float(stock['5. adjusted close'][index-1])) - 1 for index, value in enumerate(stock['5. adjusted close'])]
	stock.iloc[0,8] = math.nan
	stock['simpleReturn'].plot(figsize=(8, 5))
	plt.show()
	# Multiply mean by 250 as trading days are 250
	meanForSimpleReturn = stock['simpleReturn'].mean() * 250
	simpleReturnPercentage = round(meanForSimpleReturn * 100, 2)
	return (meanForSimpleReturn, simpleReturnPercentage)