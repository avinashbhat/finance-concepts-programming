from util import convert_dictionary_to_numpy
from alphavantage import get_time_series_daily_adjusted
from matplotlib import pyplot as plt
import math

PG = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol='PG', apikey='PQPNGOENWG0YERJ0'))
# print(type(PG['5. adjusted close'][1]))

PG['simpleReturn'] = [(float(value)/float(PG['5. adjusted close'][index-1])) - 1 for index, value in enumerate(PG['5. adjusted close'])]
PG.iloc[0,8] = math.nan
# print(PG.head())

PG['simpleReturn'].plot(figsize=(8, 5))
plt.show()

# Multiply mean by 250 as trading days are 250
meanForSimpleReturn = PG['simpleReturn'].mean() * 250
simpleReturnPercentage = round(meanForSimpleReturn * 100, 2)

print("Mean: " + str(meanForSimpleReturn))
print("Percentage: " + str(simpleReturnPercentage) + "%")

