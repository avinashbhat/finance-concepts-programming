from matplotlib import pyplot as plt
import math

# Function to return log return value for adjusted close values given of a particular stock
# Takes in series and returns a series
def log_return_mean_percentage(stock):
	stock['logReturn'] = [math.log(float(value)/float(stock['5. adjusted close'][index-1])) for index, value in enumerate(stock['5. adjusted close'])]
	stock.iloc[0,8] = math.nan
	stock['logReturn'].plot(figsize=(8, 5))
	plt.show()
	# Multiply mean by 250 as trading days are 250
	meanForLogReturn = stock['logReturn'].mean() * 250
	logReturnPercentage = round(meanForLogReturn * 100, 2)
	return (meanForLogReturn, logReturnPercentage)

def log_return_list(stockAdjustedClose):
	logReturn = [math.log(float(value)/float(stockAdjustedClose[index-1])) for index, value in enumerate(stockAdjustedClose)]
	logReturn[0] = math.nan
	return logReturn