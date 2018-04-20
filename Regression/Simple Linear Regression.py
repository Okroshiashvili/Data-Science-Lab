"""
Created on Fri Apr 20 15:38:55 2018

@author: Nodar.Okroshiashvili
"""


#%%

# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Salary_Data.csv')
# Independent variable or feature vector
X = dataset.iloc[:, :-1].values
# Dependent variable vector
y = dataset.iloc[:, 1].values


#%%

# Splitting the dataset into the Training set and Test set

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


#%%

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression

# Create regressor object
regressor = LinearRegression()
# Fit the object to the training set
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


#%%

# Visualizing the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#%%

# Visualizing the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Here the straight line is the same as above graph but the points/observations are different


