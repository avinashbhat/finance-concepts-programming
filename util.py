import random
import numpy
import pandas


# Util function to generate random number between two indices
def generate_random_number(startingIndex, endingIndex):
	return random.randint(startingIndex, endingIndex)

# Util function to generate a random matrix, provided the starting and 
# ending indices 
def generate_random_matrix(startingIndex, endingIndex, xrows, yrows):
	return numpy.random.randint(startingIndex, endingIndex, (xrows, yrows))

# Util function to convert a dictionary to numpy
# Returns a pandas DataFrame
def convert_dictionary_to_numpy(dictionary):
	return pandas.DataFrame.from_dict(dictionary, orient='index')

# Util function to normalize a series
# Returns a pandas dataframe
def normalize_series_to_hundered(series):
	firstElement = float(series[0])
	series = [(float(element)/firstElement)*100 for element in series]
	return series
