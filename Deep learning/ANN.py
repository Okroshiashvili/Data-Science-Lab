"""
Created on Tue Mar 20 22:08:05 2018

@author: Nodar.Okroshiashvili
"""

"""

Artificial Neural Network with Stochastic Gradient Descent

"""

#%%

# Install necessary packages

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras



#%%

# Part I

# Data Preprocessing



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values


"""
We do not know which independent variable has the most impact on dependent variable,
and that's what ANN will do for us. It'll spot variable with higher weight.

"""

#%%

# Encoding categorical data


from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# We have two categorical variables, so we need two encoders


# Categorical variable for country
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

# Categorical variable for gender
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

# Since country is not ordinal variable we need to create three dummy variabes
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

# We need remove one dummy variable to avoid dummy variable trap
X = X[:,1:]


#%%

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling 

# Feature scaling is compulsory in deep learning due to intensive calculations
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#%%


# Part II

# Create ANN

# Import Keras and other necessary packages
import keras

# We need to import two module

# The sequential module that is required to initialize our neural network
# The dense module that is required to build the layers of our neural network
from keras.models import Sequential
from keras.layers import Dense

#%%

# Initialize the ANN, defining it as a sequence of layers
# We have two ways to initialize ANN
# First, by defining the sequence of layers 
# Second, by defining graph


# Create an object of sequential class
# Since we have classification problem, we'll call ANN object classifier
classifier = Sequential()

#%%


# Add the input layer and first hidden layer


# We choose rectifier activation function for hidden layer and
# sigmoid activation function for output layer
"""
parameter output_dim is the number of nodes in output layer.
we choose it by averaging the number of features and number of outcome.
Hence for that example we have 11 features and two outcome for dependent variable,
henceforth we need only one node for output layer and  we have (11 + 1) / 2 
nodes in hidden layer


"""

classifier.add(Dense(output_dim = 6, init='uniform', activation = 'relu', input_dim = 11))

# Adding second hidden layer
classifier.add(Dense(output_dim = 6, init='uniform', activation = 'relu'))


# Adding the output layer
classifier.add(Dense(output_dim = 1, init='uniform', activation = 'sigmoid'))

"""
We want to have probabilities of each customer leavs the bank, so we choose
sigmoid activation function for output layer

"""


#%%


# Compiling the ANN

# We apply Stochastic Gradient Descent to the whole ann


classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics =['accuracy'])

#%%


# Fit the ANN to the training set

# Epochs is the number of time we train Ann to our whole training set


classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)



#%%

# Part III

# Making predictions and model evaluation



# Predicting the Test set results
# Here predict method returns predicted probabilities
# For confusion matrix we need  binary outcome
# So we choose the threshold. Below threshold prediction is zero, above is one
y_pred = classifier.predict(X_test)

# we'll use trick to update y_pred with True/False values
y_pred = (y_pred > 0.5)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


#%%
