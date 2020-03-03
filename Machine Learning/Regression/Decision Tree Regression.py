


"""
 Decision Tree Regression

"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Importing the dataset
dataset = pd.read_csv('data/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values



# I don't split dataset because it's too small for that


# Fitting Decision Tree Regression to the dataset
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(np.array([[6.5]]))




# Visualizing the Decision Tree Regression results

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


"""

We have to rise the red flag because Decision Tree algorithm splits the data in rectangular forms in case of two or more variable. 
Since we have here one independent variable algorithm uses intervals.
Form the graph it's clear that algorithm uses either infinite intervals or there is other problem.
We don't have first problem, because it impossible to use infinite interval between two points,
so we have another problem.
The problem here is that the Decision Tree algorithm in not continuous.

"""


# Visualizing the Decision Tree Regression results (higher resolution)

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


"""

This is the TRUE regression line.
All the points between 5.5 and 6.5 predicted values will be 150,000 as it is the average of this interval

Generally, Decision Tree model in not interesting in one dimension,
but in two or more dimensions it's very powerful.

"""
