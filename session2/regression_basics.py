################  easy_install -U statsmodels   ###################   type this into terminal/command prombt

import statsmodels.api as sm
m = sm.OLS(gpa["College"], gpa["ACT"])
results = m.fit()
print(results.summary())

m = sm.OLS(gpa["College"], gpa[["HS","ACT"]])
results = m.fit()
print(results.summary())

import matplotlib.pyplot as plt
plt.plot(results.predict(),'bo')


