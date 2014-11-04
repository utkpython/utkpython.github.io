
#####statsmodels install instructions
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


gpa=pd.read_csv('collegegpa.csv')
gpa["College"]
gpa[1:1]     
gpa[1:3]
gpa["College"]
gpa[["HS", "ACT"]]



m = smf.ols('College ~ ACT', data = gpa)
results = m.fit()
print(results.summary())

m = smf.ols('College ~ ACT + HS', data = gpa)
results = m.fit()
print(results.summary())


plt.plot(results.predict(),'bo')
######anova example

comp = smf.ols('College ~ ACT + HS + APHours + Height + ACT + KnownLanguages', data = gpa).fit()
simp = smf.ols('College ~ ACT + APHours + Height', data = gpa).fit()

from statsmodels.stats.api import anova_lm
anova_lm(simp, comp)

##############
# Load data
url = 'http://vincentarelbundock.github.io/Rdatasets/csv/HistData/Guerry.csv'
dat = pd.read_csv(url)

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print results.summary()
plt.plot(results.predict(),"bo")

