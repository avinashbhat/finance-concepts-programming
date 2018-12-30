from portfolio_rate_of_return import getPortfolioRateofReturn, displayRateOfReturn
from util import convert_dictionary_to_numpy
from alphavantage import get_time_series_daily_adjusted
from constants import apikey

# stockData = convert_dictionary_to_numpy(get_time_series_daily_adjusted(symbol='PG', apikey=apikey))

# mean, percentage = simple_return(stockData)
# print(mean)
# print(percentage)

# mean, percentage = log_return(stockData)
# print(mean)
# print(percentage)

# print(getPortfolioRateofReturn(['PG', 'F'], [0.5, 0.5]))
displayRateOfReturn(['^GSPC', 'IXIC', '^GDAXI', '^FTSE'])