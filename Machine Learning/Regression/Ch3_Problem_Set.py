"""
Created on Sat Aug  4 12:47:39 2018

@author: N.Okroshiashvili
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.graphics.regressionplots import influence_plot as lev_plot
import statsmodels.api as sm



################################################################################

#    8 დავალება

# open dataset
df = pd.read_csv('Auto.csv')

# extract dependent and independent variable
y = df.iloc[:, 0].values
X = df.iloc[:,3].values

# add constant term
X = sm.add_constant(X)

# Regressor object
regressor = sm.OLS(y,X)


# fit the model
result = regressor.fit()

# print the result
result.summary()

# make in sample prediction
y_pred = result.predict(X)


# Plot
plt.scatter(X[:,1], y, color = 'red')
plt.plot(X[:,1], y_pred, color = 'blue')
plt.title('mpg vs horsepower')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.show()


# Leverage and influence
lev_plot(result)

# Residuals
residual = y - y_pred

# Residual Box-plot
plt.boxplot(residual)

# Q-Q plot for residual
stats.probplot(residual, plot=plt, dist='norm')
plt.title("Q-Q plot for residuals")
plt.show() 


################################################################################

#   9 დავალება

#                           Multiple Linear Regression

# open dataset
df = pd.read_csv('Auto.csv')


# scatterplot matrix
pd.scatter_matrix(df.iloc[:,:8],alpha=0.2, figsize=(7,7), diagonal='kde')

sns.pairplot(df.iloc[:,:8])

sns.pairplot(df.iloc[:,:8], vars = ["mpg", "horsepower", "weight", "acceleration"], diag_kind='kde')


# Correlation
correlation = df.iloc[:,:8].corr()


# extract dependent and independent variable
y = df.iloc[:, 0].values
X = df.iloc[:,:8].values

# add constant term
X = sm.add_constant(X)

# Regressor object
regressor = sm.OLS(y,X)


# fit the model
result = regressor.fit()

# print the result
result.summary()

# make in sample prediction
y_pred = result.predict(X)

# Residuals
residual = y - y_pred

# Leverage and influence
lev_plot(result)


# Residual Box-plot
plt.boxplot(residual)

# Q-Q plot for residual
stats.probplot(residual, plot=plt, dist='norm')
plt.title("Q-Q plot for residuals")
plt.show() 


#   e და f დამრჩა გასაკეთებელი



################################################################################


#     11 დავალება


# set random seed
np.random.seed(1)

# generate sample from standard normal
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# define regressor object and fit the model without the intercept
# regress y onto x
regressor = sm.OLS(y,x)
result = regressor.fit()

# print result summary
result.summary()


# regress x onto y without intercept
regressor1 = sm.OLS(x,y)
result1 = regressor1.fit()

# print the result
result1.summary()




################################################################################


#     13 დავალება  


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# set random seed
np.random.seed(1)

# draw sample from standard normal
X = np.random.standard_normal(100)

# draw some normal noise
eps = np.random.normal(loc=0.0, scale=0.25, size=100)

#  true Y
Y = (-1) + (0.5 * X) + eps

# scatter plot
plt.scatter(X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# add constant term
X = sm.add_constant(X)

# Regressor object
regressor = sm.OLS(Y,X)

# fit the model
result = regressor.fit()

# print the result
result.summary()

# make in sample prediction
y_pred = result.predict(X)

# Residuals
residual = Y - y_pred

# Plot Y vs Y_hat
label = ['regression line', 'true Y']
plt.scatter(X[:,1],Y, color='red')
plt.plot(X[:,1],y_pred, color='blue')
plt.title('Y vs Y_hat')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(label, loc='best')
plt.show()


# Polynomial regression

# add X^2 term in the dataset
X_2 = [x**2 for x in X[:,1]]

# add new column to the numpy array
X = np.insert(X,2,X_2,axis=1)

# Regressor object
regressor1 = sm.OLS(Y,X)

# fit the model
result1 = regressor1.fit()

# print the result
result1.summary()

# Quadratic term doesn't improve the model. That was expected.



################################################################################


#     14  დავალება 


# set random seed
np.random.seed(1)

# draw sample from uniform distribution
X1 = np.random.uniform(size=100)

# add some noise from normal distribution
X2 = 0.5 * X1 + np.random.normal(size=100)/10

# y is linear combination of x's and plus some noise
Y = 2 + 2 * X1 + 0.3 * X2 + np.random.normal(size=100)

# correlation
np.corrcoef(X1,X2)

# scatter plot btw X1 and X2
plt.scatter(X1,X2)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Correlation X1 - X2 ')
plt.show()


# concatenate two preddictor
X = np.concatenate((X1.reshape(-1,1),X2.reshape(-1,1)),axis=1)

# add constant term
X = sm.add_constant(X)

# Regressor object
regressor = sm.OLS(Y,X)

# fit the model
result = regressor.fit()

# print the result
result.summary()

# make in sample prediction
y_pred = result.predict(X)

# Residuals
residual = Y - y_pred

# condition number does not indicate multicollinearity
# https://en.wikipedia.org/wiki/Condition_number
# აქ რაღაცეებია კიდევ ჩასატარებელი ოპერაციები და თუ დაგაინტერესებთ დავამატებ

infl = result.get_influence()
