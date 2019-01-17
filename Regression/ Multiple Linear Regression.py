"""
Created on Tue Jun 26 15:40:47 2018

@author: Nodar.Okroshiashvili
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t as t_stat
from scipy.stats import f as f_stat

df = pd.read_csv('wage1.csv')

##################################################

## Pair plot to see relationships btw variables
#new_df = df[['wage', 'hours', 'educ', 'exper']]
#sns.pairplot(new_df)

##################################################

# Separate Y and X matrix from dataset
Y = np.array(df['wage'])

X = np.array(df.iloc[:,[0,1,2,3,4,5,6]])
# Insert ones to estimate constant term
X = np.insert(X,0,np.ones(935),axis=1)
"""
Without intercept or constant term we force model to go through the origin

"""

# In this step calculate intermediate results
# Some Linear Algebra
# We have our Design Matrix X
X_T = np.transpose(X) # Transpose of X
X_T_X = np.dot(X_T,X) # Dot product of X and its transpose
X_T_X_inv = np.linalg.inv(X_T_X) # Inverse of above dot product
X_T_X_inv_X_T = np.dot(X_T_X_inv,X_T) # dot product of inverse and transpose



# Now we can estimate parameters
betas = list(np.dot(X_T_X_inv_X_T,Y))
# Convert betas matrix into dictionary with row labels
keys = list(df.iloc[:,:-1].columns.values)
keys.insert(0,'Intercept') # Insert label for intercept
# betas = dict(zip(keys,betas) # Make dictionary of betas with appropriate labels
betas = pd.DataFrame(betas,keys,dtype='float')

"""
As we already estimated parameters we can make predictions
This is in-sample predictions by using following formula: Y_hat = X * betas


"""
# First define Hat Matrix H
H = np.dot(X,X_T_X_inv_X_T)

Y_hat = np.dot(H,Y)

# Calculate Residuals r = Y - Y_hat
r = np.subtract(Y,Y_hat)


# Model Variance and Standard error
Var_e = sum([r[i]**2 for i in range(len(r))])/(len(Y)-len(keys))
SE_regression = Var_e**0.5


# Covariance Matrix
# Diagonal elements are variance of betas
Cov_mat = Var_e * X_T_X_inv
# Cov_mat = dict(zip(keys,Cov_mat))
Cov_mat = pd.DataFrame(Cov_mat, keys, dtype='float')

# Variance of betas
Var_betas = [[Cov_mat[i][i]for i in range(len(Cov_mat))], [Cov_mat[j][j]**0.5 for j in range(len(Cov_mat))]]
    
Var_betas = pd.DataFrame(Var_betas) # Variance and Standard Deviation matrix of betas

# Rename column and row labels
Var_betas.rename(columns={0:'Intercept',1:'hours',2:'IQ',3:'educ',4:'exper',5:'teenure',6:'age',7:'married'},inplace=True)
Var_betas.rename(index={0:'Variance',1:'Standard Deviation'},inplace=True) 
    

# Do some fancy stuff
Cov_mat.rename(columns={0:'Intercept',1:'hours',2:'IQ',3:'educ',4:'exper',5:'teenure',6:'age',7:'married'},inplace=True)




# T-Statistics for betas
t_statistics = [betas.loc[:,0][i] / Var_betas.loc['Standard Deviation'][i] for i in range(len(betas))]
t_statistics = pd.DataFrame(t_statistics,keys, dtype='float')


# პირველი ორი P_Value არაა სწორად
"""
იმიტომ არ იყო სწორად რომ პირველი ორი t-statistics იყო უარყოფითი და ეს
უყურებს მხოლოდ დადებითებს, ანუ მხოლოდ მოდულს ორივე კუდის

"""

# P-Values for betas
P_Values = [(1-(t_stat.cdf(abs(t_statistics[0][i]), df=(len(X)-len(keys)))))*2 for i in range(len(t_statistics))]
P_Values = pd.DataFrame(P_Values,keys)


# Confidence Intervals for betas
# Degree of Freedom = n - len(keys) = 927



# First compute lower bound of CI
CI_low = [betas[0][i] - (t_stat.ppf(1-0.025, len(X)-len(keys)) * Var_betas.loc['Standard Deviation'][i]) for i in range(len(t_statistics))]

# Upper bound of CI
CI_upper = [betas[0][i] + (t_stat.ppf(1-0.025, len(X)-len(keys)) * Var_betas.loc['Standard Deviation'][i]) for i in range(len(t_statistics))]

Confidence_Interval = list(zip(CI_low,CI_upper))
Confidence_Interval = pd.DataFrame(Confidence_Interval)
Confidence_Interval.rename(columns={0:'Lower CI',1:'Upper CI'},inplace=True)
Confidence_Interval.rename(index={0:'Intercept',1:'hours',2:'IQ',3:'educ',4:'exper',5:'tenure',6:'age',7:'married'},inplace=True)



# SS's and MS's

# Degree of Freedom
df_M = len(keys) - 1 # dof for Model
df_T = len(Y) - 1 # dof for Total
df_E = len(Y) - len(keys) # dof for residuals


# Sum of Squares
SST = sum([(Y[i] - Y.mean())**2 for i in range(len(Y))])
SSM = sum([(Y_hat[i] - Y.mean())**2 for i in range(len(Y_hat))])
SSE = sum([(Y[i] - Y_hat[i])**2 for i in range(len(Y))])

# Mean Square
MST = SST / df_T
MSM = SSM / df_M
MSE = SSE / df_E


# F-Statistics
# Checks whether model is jointly significant

F_stat = MSM / MSE
P_Value_F = f_stat.sf(F_stat,dfn=7,dfd=927)


def F_statistics():  
    crit = f_stat.ppf(q=1-0.025, dfn=7,dfd=927) # q is right tail probability
    if F_stat > crit:
        print('Reject H_0 : Model is Statistically Significant')
    else:
        print('Fail to reject H_0 : Model Sucks')

F_statistics()



# R-squared and Adjusted R-squared
R_square = SSM / SST
Adj_R_square = 1 - ((df_T / df_E)*(1-R_square))




# Model Selection
"""
Calculate Information Criteria to select the best model 
among several

"""
# Akaike Information Criteria
# Deals with the trade-off btw R_square and model simplicity
# AIC only tells model quality relative to other models
AIC = (len(X) * np.log(SSE/len(X))) + 2*len(keys) 
"""
არ ემთხვევა შესწორება უნდა

"""

