# remove the hashtags below to get the code to run

# import math

# math.cos(12)
# math.sqrt(math.cos(12))


# import numpy as np
# a = [1,2,3,4,5]
# np.mean(a)
# np.std(a)


from datetime import date
today = date.today()
christmas = date(2014,12,25)
d = (christmas - today).days

print d, "days until christmas"
