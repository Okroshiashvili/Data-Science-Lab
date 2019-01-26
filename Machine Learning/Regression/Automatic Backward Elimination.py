"""
Created on Wed Jan 31 11:33:37 2018

@author: Nodar.Okroshiashvili

"""



# Backward Elimination with P-Values only


import numpy as np
import statsmodels.formula.api as sm


# x and y are independent and dependent variables, respectively.



def beckwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0,numVars):
        regressor_OLS = sm.OLS(y,x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x



SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)


