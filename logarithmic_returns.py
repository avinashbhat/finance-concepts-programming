from matplotlib import pyplot as plt
import math


def log_helper(value):
	try:
		return math.log(value)
	except:
		return 0
def division_helper(v1, v2):
	try:
		return v1/v2
	except:
		return 0

# Function to return log return value for adjusted close values given of a particular stock
# Takes in series and returns a series
def log_return_mean_percentage(stock):
	stock['logReturn'] = [log_helper(division_helper(float(value),float(stock['5. adjusted close'][index-1]))) for index, value in enumerate(stock['5. adjusted close'])]
	stock.iloc[0,8] = math.nan
	stock['logReturn'].plot(figsize=(8, 5))
	plt.show()
	# Multiply mean by 250 as trading days are 250
	meanForLogReturn = stock['logReturn'].mean() * 250
	logReturnPercentage = round(meanForLogReturn * 100, 2)
	return (meanForLogReturn, logReturnPercentage)

def log_return_list(stockAdjustedClose):
	logReturn = [log_helper(division_helper(float(value), float(stockAdjustedClose[index-1]))) for index, value in enumerate(stockAdjustedClose)]
	logReturn[0] = math.nan
	return logReturn