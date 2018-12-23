import random
import numpy


# Util function to generate random number between two indices
def generate_random_number(startingIndex, endingIndex):
	return random.randint(startingIndex, endingIndex)


# Util function to generate a random matrix, provided the starting and 
# ending indices 
def generate_random_matrix(startingIndex, endingIndex, xrows, yrows):
	return numpy.random.randint(startingIndex, endingIndex, (xrows, yrows))
