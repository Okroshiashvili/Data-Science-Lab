"""
Created on Sat Jan 26 2019

@author: Nodar Okroshiashvili
"""



# Self Organizing Map


# Part 1 - Identify the Frauds with the Self-Organizing Map


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Credit_Card_Applications.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# We need to deal with categorical features
# In my opinion we have to convert them either in binary format
# or use some other encoding method


# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 15, sigma = 1.0, learning_rate = 0.5)
# As we have little data we create grid 10 by 10
# If we had more data we would make bigger grid to map data and 
# identify outliers or faud correctly
# "input_len" argument corresponds the number of features in dataset
# In original data set which is X, we keep customer ID in order to identify
# fradulet transactions
# "sigma" is the radius of different neighbourshoods in the grid
# "learning_rate" decides how much to weight our data during each iteration
# Higher the learning rate the higher there will be convergence


# Randomly initialize weights
som.random_weights_init(X)

# Train SOM on data
som.train_random(data = X, num_iteration = 100)




# Visualizing the results
from pylab import bone, pcolor, colorbar, plot, show

# Initialize window which will contin map
bone()
# Colorize all the winning nodes based by distance
# Mean Interneuron Distance
pcolor(som.distance_map().T)
# Above two code lines gives all the mean interneuron distances

colorbar()
# Ths gives colorbar to identify which is high mean interneuron distance
# and which low
# Based on this colorbar, we see that fraudlent transactions are white,
# as their distance is far from mean interneuron distance

# We add some marker to distinguish between customers who get approval and 
# cheated and customers who didn't get approval and cheated
markers = ['o', 's']
colors = ['r', 'g']
# Red circles corresponds to customers who didn't get approval
# Green squares corresponds customers who got approval


# Loop over all the customers and for each customer we will get the winning node
# DEpendind on whether customer got approval or not we color that node
# red if customer didn't get approval and green if got approval
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()



# Finding the frauds
mappings = som.win_map(X)

# Here I put the coordinates of faudlant transactions
# In my set up these coordinates are (5,2) but you may get different
frauds = np.concatenate((mappings[(5,2)], mappings[(6,8)]), axis = 0)
frauds = sc.inverse_transform(frauds)




# Part 2 - Going from Unsupervised to Supervised Deep Learning



# Creating the matrix of features
customers = dataset.iloc[:, 1:].values



# Creating the dependent variable
# We create matrix of zeros and then populate this matrix with the
# output of Self Organizing Map
# which show potential fraud
# We coded fraud as 1 and not fraut as 0
# So, from SOM output we have 67 potential frauds
# and 690-67 non fraud transaction
is_fraud = np.zeros(len(dataset))
for i in range(len(dataset)):
    if dataset.iloc[i,0] in frauds:
        is_fraud[i] = 1


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
customers = sc.fit_transform(customers)



# Part 3 - Now let's make the ANN!

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense


# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 2, kernel_initializer = 'uniform', activation = 'relu', input_dim = 15))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(customers, is_fraud, batch_size = 1, epochs = 2)

# Predicting the probabilities of frauds
y_pred = classifier.predict(customers)

# Add customer IDs
y_pred = np.concatenate((dataset.iloc[:, 0:1].values, y_pred), axis = 1)

# Sort the probabilities
y_pred = y_pred[y_pred[:, 1].argsort()]






