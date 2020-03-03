


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('wage1.csv')

X = df.iloc[:,[0,1,2,3,4,5,6]]

y = df.iloc[:,7]



#                         Feasible Generalized Least Squares

"""
We don't know covariance matrix, hence we either assume or estimate 
it empirically. 

If we assume the covariance matrix we have to use Weighted Least Squares
and if we estimate it empirically we have to use Feasible Generalized Least Squares

"""




"""
Instead of assuming the structure of heteroscedasticity, we may estimate it from OLS.

This method is called FGLS. First, we have to estimate covariance matrix and
second we use estimated covariance matrix instead of real covariance matrix.


There are many ways to estimate FGLS, but one common way is to assume that

" Var(u|X) = u^2 = sigma^2 * exp(beta_0 + beta_1*X_1 + .... + beta_k*X_k) "


By taking log of the both side and using u_hat^2 instead of u^2, we can estimate

" log(u_hat^2) = beta_0 + beta_1*X_1 + ... + beta_k*X_k + e "



The predicted value from this model is g_hat = log(u_hat^2).
We then convert it by taking exponential into w_hat = exp(log(u_hat^2)_hat) = u_hat_hat^2

We know can use WLS with weights 1/w_hat or 1/u_hat_hat^2
    
"""


"""

First we need to regress y on X, compute squared residuals and then
we have to take natural logarithm of these squared residuals and regress on X and 
compute residuals again and the predicted values from this model will be 
g_hat = log(u_hat^2)_hat

Taking exponent of g_hat gives w_hat = exp(g_hat) = exp(log(u_hat^2)_hat) = u_hat_hat^2

We can now use 1/w_hat as a weight


"""


# 1 Step
# y on X

X = sm.add_constant(X)                 # Add constant term
regressor = sm.OLS(y,X)                # Regressor object
result = regressor.fit()               # Fit the model to the data

result.summary()                       # Print the model summary

y_hat = result.predict(X)              # Make in sample prediction
residual = y - y_hat                   # Calculate residuals
residual_2 = residual**2               # Square of residuals
log_residual_2 = np.log(residual_2)    # Natural logarithm of squared residuals



regress_resid = sm.OLS(log_residual_2,X) # Regressor object
resid_result = regress_resid.fit()       # Regress residuals on X

resid_result.summary()                   # Model summary

res_hat = resid_result.predict(X)       # g_hat
w_hat = np.exp(res_hat)                 # w_hat


weight_FGLS = 1 / (w_hat)**0.5               # This is our weight

"""
Now this weights have to be applied for each independent variable and
rerun initial regression y on X but adjusted with weights.


Before runing regression y on X we have to generate new weighted variables

"""

y_weighted_FGLS = y * weight_FGLS

X_FGLS = df.iloc[:,[0,1,2,3,4,5]]                    # New matrix of features



X_weighted_FGLS = []
for i in X_FGLS.columns:
    X_weighted_FGLS.append(X_FGLS[i] * weight_FGLS)           # This loop goes through each feature and multiplies 
                                                   # by weight
    

X_weighted_FGLS = np.transpose(np.array(X_weighted_FGLS))    # Matrix of weighted features with no constant term
X_weighted_FGLS = pd.DataFrame(X_weighted_FGLS)
X_weighted_FGLS.rename(columns={0:'hours',1:'IQ',2:'educ',3:'exper',4:'tenure',5:'age'},inplace=True)



FGLS_regressor = sm.OLS(y_weighted_FGLS,X_weighted_FGLS)     # Regressor object
FGLS_result = FGLS_regressor.fit()                           # Regress y on weighted X

FGLS_result.summary()                                        # See the model summary

FGLS_y_hat = FGLS_result.predict(X_weighted_FGLS)            # Model in sample prediction

FGLS_residual = y_weighted_FGLS - FGLS_y_hat                 # FGLS residuals


"""
These are steps to perform FGLS. After last regression we can perform 
hypothesis testing and other tests.

While running FGLS we have to reject dummy variable as well as constant term



შეიძლება დასაჭირდეს შემოწმება რამდენად სწორია ალგორითმი
სახლში შევამოწმებ სტატაზე



To Do List:

1) Make Plots
2) Calculate intermediate results like sum of squares and mean sum of squares
3) Perform hypothesis testing
4) Perform other tests like non-linearity, normality, heteroscedasticity

"""



################################################################################


"""                 
                           Weighted Least Square
                           
                           
                           
                           
                           
In above example, we estimated empirically covariance matrix and used FGLS.
Now we make assumption about it and take education as a weight                            
                           
"""



X_WLS = df.iloc[:,[0,1,2,3,4,5]]

weight_WLS = 1 / (X_WLS['educ'])**0.5

y_weighted_WLS = y * weight_WLS

X_weighted_WLS = []
for i in X_WLS.columns:
    X_weighted_WLS.append(X_WLS[i] * weight_WLS)  # This loop goes through each feature and multiplies 
                                                  # by weight
    

X_weighted_WLS = np.transpose(np.array(X_weighted_WLS)) # Matrix of weighted features with no constant term
X_weighted_WLS = pd.DataFrame(X_weighted_WLS)
X_weighted_WLS.rename(columns={0:'hours',1:'IQ',2:'educ',3:'exper',4:'tenure',5:'age'},inplace=True)




WLS_regressor = sm.OLS(y_weighted_WLS,X_weighted_WLS)     # Regressor object
WLS_result = WLS_regressor.fit()                          # Regress y on weighted X

WLS_result.summary()                                      # See the model summary

WLS_y_hat = WLS_result.predict(X_weighted_WLS)            # Model in sample prediction

WLS_residual = y_weighted_WLS - WLS_y_hat                 # FGLS residuals


"""
ეს შევამოწმე და სწორად მუშაობს, მაგრამ კიდევ უნდა შემოწმება




To Do List:
    
რაც FGLS-ზეა დასამატებელი ის დავამატო, დანარჩენი მომაფიქრდება



"""
