"""
Created on Tue Mar 20 2018

@author: Nodar Okroshiashvili
"""

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values


"""
We do not know which independent variable has the most impact 
on the dependent variable, and that's what ANN will do for us.
It'll spot variable with higher weight.

"""



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
X = X[:, 1:]



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



# Part 2 - Now let's make the ANN!



# Importing the Keras libraries and packages

import keras
# The sequential module that is required to initialize our neural network
# The dense module that is required to build the layers of our neural network
# The dropout module that is required for regularization of the network
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

# Initialising the ANN, defining it as a sequence of layers
classifier = Sequential()

# Adding the input layer and the first hidden layer
# argument "units" is the number of neurons in first hidden layer


# To soleve overfitting problem we now use Dropout Regularization
# Droupout can be randomly applied to layers to disable them to learn too much
# We add Droup out to input layer and first hidden layer
# It's generally advised to apply these two layers


"""
parameter "units" is the number of nodes in the output layer.
we choose it by averaging the number of features and number of the outcome.
Hence, for that example, we have 11 features and two outcomes for the dependent variable,
henceforth we need only one node for the output layer and  we have (11 + 1) / 2 
nodes in the hidden layer

"""

classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
classifier.add(Dropout(rate = 0.1))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(rate = 0.1))

# Adding the output layer
# If dependent variable is categorical we create dummies for each category
# and in output layer we change argument "units = # of categories"
# and argument "activation = softmax"
# Softmax is sigmoid function for categorical dependent variable

classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))


"""
We want to have probabilities of each customer leaves the bank, so we choose sigmoid activation function for the output layer

"""



# Compiling the ANN
# Untill this step weights in layers are still initialized and not optimized
# optimizer argument do this job
# We use stochastic gradient descent algorithm named "adam"
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
# Epochs is the number of time we train Ann to our whole training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)



# Part 3 - Making predictions and evaluating the model




# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



# Make some new prediction

"""Predict if the customer with the following informations will leave the bank:
Geography: France
Credit Score: 600
Gender: Male
Age: 40
Tenure: 3
Balance: 60000
Number of Products: 2
Has Credit Card: Yes
Is Active Member: Yes
Estimated Salary: 50000"""
new_prediction = classifier.predict(sc.transform(np.array([[0.0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])))
new_prediction = (new_prediction > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)




# Part 4 - Evaluating, Improving and Tuning the ANN




# Evaluating the ANN


# Include K-Fold Cross Validation into Keras
# We use Keras wraper to do so


from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense


def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier

# Create new classifier which will be global classifier
classifier = KerasClassifier(build_fn = build_classifier, batch_size = 10, epochs = 100)

# Use Cross Validation
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)

# Compute the mean and variance of these accuracies
mean = accuracies.mean()
variance = accuracies.std()



#        Tuning the ANN Hyper-parameters to achieve higher accuracy


from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense


def build_classifier(optimizer):
    classifier = Sequential()
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier

# Create new classifier which will be global classifier
classifier = KerasClassifier(build_fn = build_classifier)


# We create dictionary which contains hyper parameters to be optimized

parameters = {'batch_size': [25, 32],
              'epochs': [100, 500],
              'optimizer': ['adam', 'rmsprop']}

# Implement Grid Search
grid_search = GridSearchCV(estimator = classifier,
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 10)

# Fit grid search to training set
grid_search = grid_search.fit(X_train, y_train)


# Extract best hyper-parameter and best accuracy selection
best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_ 

# Best hyper-parameters are: 
# batch_size = 32
# epochs = 500
# optimizer = 'adam'
# In this settings accuracy is 0.84875




