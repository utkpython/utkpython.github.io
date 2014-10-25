from ystockquote import get_historical_prices
from datetime import date

preliminaryData = get_historical_prices('YHOO','2014-01-01','2014-10-20')

#print type(preliminaryData)
