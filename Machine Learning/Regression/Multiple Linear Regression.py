"""
Created on Wed Jan 31 11:43:15 2018

@author: Nodar.Okroshiashvili

"""

#%%


# Multiple Linear Regression



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#%%

# Encoding categorical variable

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()

X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


# Avoiding the Dummy Variable Trap

X = X[:, 1:]

# First colon means that we choose all the rows, and 1: means we choose all the columns
# but not first columns

#%%

# Splitting the dataset into the Training set and Test set

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# We don't need to apply Feature Scaling

#%%

# Fit the model to the Training set

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, y_train)

# Test the model performance on test set
y_pred = regressor.predict(X_test)


#%%


"""

To build good model there are several methods how we can choose
optimal variables.

They are:

1. All-in
2. Backward Elimination
3. Forward Selection
4. Bidirectional Elimination
5. Score Comparison



Here I put Backward Elimination algorithm, others implementation are up to you


Backward Elimination algorithm will choose independent variables, so called explanatory or variables
with statistical significance more then pre-defined.

I'll also add backward elimination algorithm as a stand-alone file

"""


# Statsmodels API does not considers constant term in backward elimination process, 
# so we have to add unity column in our dataset

import statsmodels.formula.api as sm

X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)


# Create matrix of optimal features
X_opt = X[:,[0, 1, 2, 3, 4, 5]]

# I set significance level at 0.05 as conventional

# Fit the model
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()


# Print model summary
print(regressor_OLS.summary())

# From summary we see that dummy variable has the highest P-Value,
# so we have to remove it


# Define new optimal features
X_opt = X[:[0, 1, 3, 4, 5]

# Fit the model
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()


# Print model summary
print(regressor_OLS.summary())


# Define new optimal features
X_opt = X[:[0, 3, 4, 5]

# Fit the model
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()


# Print model summary
print(regressor_OLS.summary())


# Define new optimal features
X_opt = X[:[0, 3, 5]

# Fit the model
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()


# Print model summary
print(regressor_OLS.summary())


# Define new optimal features
X_opt = X[:[0, 3]

# Fit the model
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()


# Print model summary
print(regressor_OLS.summary())


# We see that only constant term and R&D spend drives the Profit for that company

# The model is finished!











