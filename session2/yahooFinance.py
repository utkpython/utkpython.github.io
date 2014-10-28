from ystockquote import get_historical_prices
from datetime import date
from pylab import *

data = get_historical_prices("IBM","2014-01-01","2014-10-20")

smaller_data = {}
for dates in data:
    smaller_data[dates] = data[dates]['Adj Close']


dates = smaller_data.keys()
dates.sort(key=lambda dates: dates)

prices = [smaller_data[date] for date in dates]

plot(prices)
show(plot)
