"""
Created on Thu Aug 30 13:48:52 2018

@author: nokroshiashvili
"""


"""
simple Linear Regression with Gradient Descent

"""


import pandas as pd


# Open dataset
df = pd.read_excel('data.xlsx')

# Conver Pandas DataFrame into List
df = df.values

"""
In our case Y = b + m*X
where, m is slope and b is intercept


To find best estimates for slope and intercept we need to define 
cost function or error function.

In our case it's C(b,m) = 1/N * sum[y - y_hat]^2


"""

# Function computes error for a line given points

def cost_fun(b,m,points):
    totalError = 0
    for i in range(len(points)):
        # iteration goes through each point for ind and dep variable
        x = points[i, 0]
        y = points[i, 1]
        totalError = totalError + (y - (m*x + b)) ** 2
    return totalError / float(len(points))

# To check the function put any values for b and m and also put your df
cost_fun(1.2,1.3,df)


"""
To run Gradient Descent we need first order derivatives of our 
cost function with respect to slope and intersept


Taking derivative gives us:
    
    d/dm = 2/N * sum[-x(y - (m*x + b))]
    d/db = 2/N * sum[-(y - (m*x + b))]

"""

# Function computes the direction of Gradient for any initial guess.
# b_current and m_current are our initial guess for gradients 
# what we put in our gradient function
def gradient(b_currnet, m_current, points, learningRate):
    # b_gradient and m_gradient will adjust for each iteration
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    # Calculate the new value of gradient
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient = b_gradient + (-(2/N) * (y - ((m_current * x) + b_currnet)))
        m_gradient = m_gradient + (-(2/N) * x * (y -(m_current * x) + b_currnet))
    # These are adjusted new estimates
    # Learning Rate is step size for gradient iteration
    new_b = b_currnet - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

# Function gives new estimates for b and m adjusted by the value of gradient 
gradient(0,-1,df, 0.001)




# We need to run our gradient function for number of iteration to 
# obtain optimal values for estimates
def gradient_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    
    for i in range(num_iterations):
        b, m = gradient(b, m, df, learning_rate)
    return [b,m]


# If Learning Rate is 0.001 or more (0.01, 0.1) function does not work due to 
# division by zero
gradient_runner(df,0,-1,0.0001,2000)



# Function does all the above steps all together

def run():
    points = df
    learning_rate = 0.000005
    # Initial guesses for b and m
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    print("Starting Gradient Descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, cost_fun(initial_b, initial_m, points)))
    [b, m] = gradient_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, cost_fun(b, m, points)))



# To tune the parameters change them only inside run() function
if __name__ == '__main__':
    run()

