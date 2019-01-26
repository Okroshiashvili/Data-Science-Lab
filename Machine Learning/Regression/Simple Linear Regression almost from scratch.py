"""
Created on Wed May 23 13:34:04 2018

@author: Nodar.Okroshiashvili
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as t_stat
from scipy import stats
# Load file
df = pd.read_csv('data.csv')

# Seperate X and Y values
X = list(df['YearsExperience'].values)
Y = list(df['Salary'].values)

"""
In Simple Linear Regression we assume functional form of regression
line as it is linear and we try to estimate parameters. Since that 
Simple Linear Regression is parametric approach of estimation


To ensure further that our assumption about linearity holds 
let see the plot

"""


plt.figure(figsize=(10,5))
plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Salary vs Experience')
plt.show()

"""
We clearly see the linear dependence, so least square has to be good approach

It's worth to note that the least square approach estimates parameters in such
a way to minimize residual sum of squares, RSS. 

"""

# Descriptive Statistics
def des_stat(arr):
    minimum = min(arr)
    maximum = max(arr)
    mean = sum(arr) / len(arr)
    median = (sorted(arr)[len(arr) // 2] + sorted(arr)[-(len(arr) // 2 + 1)]) / 2
    mode = max(sorted(arr), key = arr.count)
    if len(arr) % 2 == 0:
        lower_half = arr[:len(arr) // 2]
        upper_half = arr[len(arr) // 2:]
    else:
        lower_half = arr[:arr.index(median)]
        upper_half = arr[arr.index(median)+1:]
    Q1 = (lower_half[len(lower_half) // 2] + lower_half[-(len(lower_half) // 2 + 1)]) // 2
    Q2 = median
    Q3 = (upper_half[len(upper_half) // 2] + upper_half[-(len(upper_half) // 2 + 1)]) // 2
    IQR = Q3 - Q1
    Variance = sum([(arr[i] - mean)**2 for i in range(len(arr))]) / (len(arr)-1)
    Standard_deviation = Variance**0.5
    print("Minimum : {}".format(minimum), "Maximum : {}".format(maximum),
          "Mean : {}".format(mean), "Median : {} ".format(median),
          "Mode : {}".format(mode), "Q1 : {}".format(Q1),
          "Q2 : {}".format(Q2), "Q3 : {}".format(Q3),
          "IQR : {}".format(IQR), "Variance : {}".format(Variance),
          "Standard Deviation : {}".format(Standard_deviation),sep="\n")    


des_stat(X)
des_stat(Y)   

""" 
As stated above we have to estimate parameters, beta_0 and beta_1 in such a
way that to have minimum RSS. To do this we need some calculus and algebra and
have formula for coefficient estimates.

"""

mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)


def predict(X, Y, df):
    
    # Estimate coefficients
    beta1 = sum([(X[i] - mean_X)*(Y[i] - mean_Y) for i in range(len(X))]) / sum([(X[i] - mean_X)**2 for i in range(len(X))])
    beta0 = mean_Y - beta1 * mean_X
    
    # Calculate fitted values
    y_hat = [beta0 + beta1*X[i] for i in range(len(X))]
    
    # Calculate model Variance and Standard Error
    Var_e = sum([(Y[i] - y_hat[i])**2 for i in range(len(Y)) ]) / (len(Y) -2)
    SE_regression = Var_e**0.5
    
    # Calculate residuals and internally studentized residuals
    residuals = [Y[i] - y_hat[i] for i in range(len(Y))]
    studentized_residuals = [residuals[i]/SE_regression for i in range(len(residuals))] 
    
    #RSE = SE_regression
    # RSE is an estimate of the standard deviation of ephsilon
    RSS = sum([(Y[i] - y_hat[i])**2 for i in range(len(Y)) ])
    RSE = (RSS / (len(X) - 2))**0.5
    
    # Variance and Standard Errors for coefficients
    Var_beta1 = Var_e / (sum([(X[i] - mean_X)**2 for i in range(len(X))]))
    SE_beta1 = Var_beta1**0.5
    Var_beta0 = Var_e * ((1/len(X)) + (mean_X**2 / (sum([(X[i] - mean_X)**2 for i in range(len(X))]))))
    SE_beta0 = Var_beta0**0.5
    
    # T-statistic for coefficients
    t_beta0 = beta0 / SE_beta0
    t_beta1 = beta1 / SE_beta1
    
    # P-Values for coefficients
    P_beta0 = (1-(t_stat.cdf(t_beta0,df=28)))*2
    P_beta1 = (1-(t_stat.cdf(t_beta1,df=28)))*2
    
    # Confidence intervals for coefficients
    CI_beta0_L = beta0 - (t_stat.ppf(1-0.025, len(X)-2) * SE_beta0)
    CI_beta0_U = beta0 + (t_stat.ppf(1-0.025, len(X)-2) * SE_beta0)
    CI_beta0 = [CI_beta0_L,CI_beta0_U]
    CI_beta1_L = beta1 - (t_stat.ppf(1-0.025, len(X)-2) * SE_beta1)
    CI_beta1_U = beta1 + (t_stat.ppf(1-0.025, len(X)-2) * SE_beta1)
    CI_beta1 = [CI_beta1_L, CI_beta1_U]
    
    # SST = SSM + SSE
    SST = sum([(Y[i] - mean_Y)**2 for i in range(len(Y))])  # Sum of Squares Total
    SSM = sum([(y_hat[i] - mean_Y)**2 for i in range(len(Y))]) # Sum of Squares Model or SSR
    SSE = sum([(Y[i] - y_hat[i])**2 for i  in range(len(Y))]) # Sum of Squares Errors or SSR
    
    # Calculate degrees of freedom
    dof_M = 1 # Degrees of Freedom for Model
    dof_T = len(X) - 1 # Degrees of Freedom for Total
    dof_R = len(X) - 2 # Degrees of Freedom for Residuals
    
    # Mean Squares
    # Use global to use that variable outside the function
    global MSM
    global MSE
    MST = SST / dof_T # Mean Squares Total
    MSM = SSM / dof_M # Mean Squares Model
    MSE = SSE / dof_R # Mean Squares Error
    RMSE = MSE**0.5 # Root MSE is standard deviation of error term
    
    # R Squared
    R_squared = SSM / SST
    
    # adjusted R_ squared = 1 - (((1-R_squared)*(len(X)-1))/(len(X)-1-1))
    adjusted_R_squared = 1 - ((SSE/SST)*(len(X)-1) / (len(X) - 1-1))
    

    # Covariance and Correlation Coefficient
    covariance = sum([(X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X))])/(len(X)-1)
    stdv_X = (sum([(X[i] - mean_X)**2 for i in range(len(X))]) / (len(X) - 1))**0.5
    stdv_Y = (sum([(Y[i] - mean_Y)**2 for i in range(len(Y))]) / (len(Y) - 1))**0.5
    corr = covariance / (stdv_X * stdv_Y)
    # R_squared = corr**2
    
    # Calculate leverage and influence
    leverage = (1 / (len(X)-1)) * np.array([((X[i] - mean_X)/stdv_X)**2 for i in range(len(X))]) + (1/len(X))
    influence = residuals * leverage / (1 - leverage)
    leverage = leverage.tolist()
    influence = influence.tolist()
    
    # I use internaly studentized residuals as it gives very approximate result
	# instead of externally studentized residuals
    DFFITS = (studentized_residuals[2]) * (leverage[2] / (1 - leverage[2]))**0.5 
    
    # Append initial df from calculated results
    df['index'] = df.index
    df['fitted_values'] = y_hat
    df['residuals'] = residuals
    df['studentized_residuals'] = studentized_residuals
    df['leverage'] = leverage
    df['influence'] = influence
    df['DFFITS'] = DFFITS
    
    # Print Results for coefficients
    print("Beta_0", 10 * ' ' ,"Beta_0 : {}".format(beta0), "Std.error : {}".format(SE_beta0),
          "t-statistic : {}".format(t_beta0), "P-Value : {}".format(P_beta0),
          "Lower CI {} - Upper CI {}".format(CI_beta0[0],CI_beta0[1]),sep='\n')
    print(70 * '-')
    print("Beta_1", 10 * ' ' ,"Beta_1 : {}".format(beta1), "Std.error : {}".format(SE_beta1),
          "t-statistic : {}".format(t_beta1), "P-Value : {}".format(P_beta1),
          "Lower CI {} - Upper CI {}".format(CI_beta1[0],CI_beta1[1]),sep='\n')    
    
    # Print Summary Statistics for Model
    print(10 * ' ', 70 * '-', sep='\n')
    print('Model Summary', 10 * ' ', "SST : {}".format(SST), "SSM : {}".format(SSM),
          "SSE : {}".format(SSE), "SST = SSM + SSE", 
          "R-squared : {}".format(R_squared), 
          "Adjusted R-squared : {}".format(adjusted_R_squared),
          "Covariance : {}".format(covariance),
          "Correlation coefficient : {}".format(corr), sep='\n')
    
 

predict(X,Y,df)    



#################################################

# Covariance and Correlation coefficient
corr_coeff = ((len(X) * sum([X[i]*Y[i] for i in range(len(X))]))- (sum(X)*sum(Y))) / ((((len(X) * sum([X[i]**2 for i in range(len(X))]))) - (sum(X)**2)) * (((len(Y)*sum([Y[i]**2 for i in range(len(Y))]))) - (sum(Y)**2)))**0.5

""""
R_squred = corr**2 

"""

    
################################################
 
# For F statistics

def F_Statistics():

    F_calculated = MSM / MSE
    crit = stats.f.ppf(q=1-0.05, dfn=1, dfd=28)
    if F_calculated > crit:
        print("Reject H_0: Model is statistically significant ")
    else:
        print("Fail to reject H_0: Model sucks")

F_Statistics()

###############################################
    
    
"""
plots leverage and influance

"""


def plot_influance():
    
    fig = plt.figure(figsize=(10,8))
    
    ax1 = fig.add_subplot(2,1,1)
    ax1.bar(df.index,df['leverage'])
    plt.title('Leverage')

    
    ax2 = fig.add_subplot(2,1,2)
    ax2.bar(df.index,df['influence'])
    plt.title('Influence')
    
plot_influance()




##############################################

"""
Residuals plots

"""

def res_plot():
    
    fig = plt.figure(figsize=(15,8))
    
    ax1 = fig.add_subplot(2,3,1)
    ax1.boxplot(df['residuals'])
    plt.title('Residuals Boxplot')    
        
    ax2 = fig.add_subplot(2,3,2)
    ax2.scatter(X, Y, color='black')
    ax2.plot(X,df['fitted_values'], color='red')
    plt.title('Actual vs Fitted')    
       
    # For Non-Linearity
    ax3 = fig.add_subplot(2,3,3)
    ax3.scatter(df['YearsExperience'], df['residuals'])
    plt.axhline(y=0, color='k')
    plt.title('Residuals vs X')
       
    ax4 = fig.add_subplot(2,3,4)
    ax4.scatter(df.index,df['residuals'])
    plt.axhline(y=0, color='k')
    plt.title('Residuals by Observation Number')
        
    # For Homoscedasticity
    ax5 = fig.add_subplot(2,3,5)
    ax5.scatter(df['fitted_values'],df['residuals'])
    plt.axhline(y=0, color='k')
    plt.title('Residuals against Y_Hat')
    
    ax6 = fig.add_subplot(2,3,6)
    ax6.scatter(df['fitted_values'], df['studentized_residuals'])
    plt.axhline(y=0, color='k')
    plt.title('Studentized Residuals vs Fitted')    
    
res_plot()

#############################################

"""
Q-Q Plot for residuals

"""

def qq_plot():
    
    stats.probplot(df['residuals'], plot=plt, dist='norm')
    plt.title("Q-Q plot for residuals")
    plt.show()    
 
qq_plot()
