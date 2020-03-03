


"""

  Backward Elimination with P-Values only
 
    
This means that we perform backward elimination and only take a look 
P-Values, or we exclude variables based on their P-Values. 

"""

import pandas as pd
import numpy as np
import statsmodels.api as sm


# Open dataset and separate X and Y variable
df = pd.read_csv('data/wage1.csv') 


# Extract independent variables and convert them into numpy array while preserving
# variable order
X = df.iloc[:,[0,1,2,3,4,5,6]].values


# Extract dependent variable
y = df['wage'].values



# x and y are independent and dependent variables, respectively.



def backwardElimination(x, sl):
    """
    The function "backwardElimination" takes two arguments, 
    one is vector of features and second is significance level above which we
    reject one or more features
    
    """
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
X_optimal = X[:, [0, 1, 2, 3, 4, 5,6]]

X_modeled = backwardElimination(X_optimal, SL)
# Returns matrix of optimal independent variables



