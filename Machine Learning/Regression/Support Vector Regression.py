


"""

 Support Vector Regression

"""



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Importing the dataset
dataset = pd.read_csv('data/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values



# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1,1))



# Fitting SVR to the dataset
# As we have no linear problem we have to use non-linear kernel
# Radial Bases Function (rbf)

regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)


# Predicting a new result
# Predicted values is in scaled format, so we need to "re-scale" to return it in original format
y_pred = regressor.predict([[6.5]])
# Rescales prediction 
y_pred = sc_y.inverse_transform(y_pred)


# Visualizing the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('SVR')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""
SVR algorithms cannot deal feature scaling itself. We have to do it ourselves.

We see that at the CEO level the curve doesn't goes. 
This is because the algorithm considers it as an outliers.
This is due to penalty parameter

"""


# Visualizing the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()





