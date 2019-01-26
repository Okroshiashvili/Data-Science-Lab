"""
Created on Tue Jun 26 11:57:48 2018

@author: Nodar.Okroshiashvili

"""



# Backward Elimination with P-Values and Adjusted R Squared


import pandas as pd
import numpy as np
import statsmodels.formula.api as sm



df = pd.read_csv('wage1.csv')

X = df.iloc[:,[0,1,2,3,4,5,6]].as_matrix()

y = df['wage'].as_matrix()



# x and y are independent and dependent variables, respectively.
# SL is significance level


def backwardElimination(x, SL):
    """
    Performs backward elimination based on P-Value and adjusted R squared
    len(X[0])
    """
    numVars = len(x[0])
    temp = np.zeros((len(x), 7)).astype(int) # Matrix of zeros
    """
    This matrix of zeros will be populated by the values from X - vector of features
    
    """
    
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit() # regressor object
        maxVar = max(regressor_OLS.pvalues).astype(float)  # maximum among P-Values
        adj_R_before = regressor_OLS.rsquared_adj.astype(float) # Adjusted R squared
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:, j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y,x).fit()
                    adj_R_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adj_R_before >= adj_R_after):
                        x_rollback = np.hstack((x, temp[:, [0, j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print(regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x


SL = 0.05  # Significance Level
X_optimal = X[:, [0, 1, 2, 3, 4, 5,6]]  # Vector of independent variables

# Returns optimal independent variables but with changed order
# Take care not to be mistaken by the column indexing as the result from
# X_Modeled does not coincide original X
X_Modeled = backwardElimination(X_optimal, SL)
