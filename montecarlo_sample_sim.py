import numpy
import matplotlib.pyplot as plt 

rev_m = 170
rev_stdev = 20
iterations = 1000


rev = numpy.random.normal(rev_m, rev_stdev, iterations)
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

COGS = -(rev * numpy.random.normal(0.6, 0.1))
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()

print(COGS.mean(), COGS.std())

gross_profits = rev + COGS
plt.figure(figsize=(15, 6))
plt.plot(gross_profits)
plt.show()
print(max(gross_profits), min(gross_profits), COGS.mean(), COGS.std())

plt.figure(figsize=(15, 6))
plt.hist(gross_profits, bins=[40, 50, 60, 70, 80, 90, 100, 110, 120])
plt.show()

plt.figure(figsize=(15, 6))
plt.hist(gross_profits, bins=20)
plt.show()