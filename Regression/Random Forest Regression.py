"""
Created on Fri Apr 27 15:36:10 2018

@author: Nodar.Okroshiashvili
"""

"""

 Random Forest Regression

"""




# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#%%

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
# n_estimator is the parameter which show # of tree in the forest

regressor.fit(X, y)


# Predicting a new result
y_pred = regressor.predict(6.5)

#%%

# Visualizing the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Random Forest Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


"""

We get more steps in the stairs by having several Decision Trees.
Therefore we have more splits than in case of one Decision Tree
If we add more three this does not mean we get even more steps on the stairs.
As we add more trees the more converge to its ultimate average

"""