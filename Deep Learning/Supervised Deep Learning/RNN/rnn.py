


# Recurrent Neural Networks



# Part 1 - Data Preprocessing


import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

# Importing the training set
dataset_train = pd.read_csv('data/Google_Stock_Price_Train.csv')

# Separate training set
training_set = dataset_train.iloc[:, 1:2].values


# Feature Scaling to optimize the process

sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)





# Creating a data structure with 60 timesteps and 1 output
# This means that RNN will use 60 timestamp backward to learn the trend and
# use 1 output to make prediction
X_train = []
y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])

  
# X_train contains first 60th values of time series
# y_train contains points from time t+1 and forward
# This for loop seems like taking first difference but not for
# whole data but only for 60 point. so slicing window equal to 60

X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))



# Part 2 - Building the RNN


# Initializing the RNN
regressor = Sequential()



# Adding the first LSTM layer and some Dropout regularization

regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
# "units" argument is the number of the LSTMs themselves
# or the number of memory units you want to have in LSTM
# Moreover, units=50 gives us high dimensionality
# in order to catch the price trend more accurately

# "return_sequence" argument is set to True because we build stacked
# LSTM and adding extra layers

# "input_shape" argument is the shape of our dataset X_train


regressor.add(Dropout(0.2))
# Dropout rate is the rate at which we drop or ignore layers in LSTM
# This means that 10 neurons will be ignored at each iteration


# Adding a second LSTM layer and some Dropout regularization
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularization
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularization
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
# This is classic fully connected layer
# units here is the price of stock at time t+1
regressor.add(Dense(units = 1))

# Compiling the RNN
# As we have regression problem here, we use mean squared error
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training Set
regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)



# Part 3 - Making the predictions and visualizing the results



# Getting the real stock price of 2017
dataset_test = pd.read_csv('data/Google_Stock_Price_Test.csv')

# This is ground truth  or real price of stock in January
real_stock_price = dataset_test.iloc[:, 1:2].values



# Getting the predicted stock price of 2017
# Conatenate training and test set
# Concatenation is necessary in order to get 60 previous inputs
# for each day of January 2017 or our test data set
# We have to concatenate original data frames not scaled ones
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)

# Load 60 previous day
# Lower bound will be january 3rd, 2017 minus 60
# Upper bound is 60 previous days before this last day of january 2017
# or last index of whole dataset or dataset_total
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values

# Reshape and scale inputs
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

# With this loop we'll get 60 previous inputs for each of the
# stock prices of January 2017 which contains 20 days
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
    

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))


predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)



# Evaluate the model



# We need to calculate RMSE

# This RMSE is in absolute terms
rmse = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))

# We need to divide RMSE by the range of stock price during January 2017
range_stock_price = real_stock_price.max() - real_stock_price.min()

# This is RELATIVE ERROR
relative_rmse = rmse / range_stock_price


# Visualizing the results
plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.grid()
plt.legend()
plt.show()



