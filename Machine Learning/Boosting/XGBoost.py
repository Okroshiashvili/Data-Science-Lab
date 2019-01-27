"""
Created on Thu Mar 29 2018

@author: Nodar Okroshiashvili
"""




"""
XGBoost

"""



# Data Preprocessing



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values




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



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



"""

Applying XGBoost

"""
import xgboost as xgb


dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test,y_test)

# Model Hyper Parameters
# These paramters should be tuned for better performance
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic',
         'eval_metric':'auc'}

num_round = 10

# Fit the model
classifier = xgb.train(param, dtrain, num_round)



# Predicting the Test set results
y_pred = classifier.predict(dtest)

# By default we got class probabilities
# This code turns it into binary outcome
y_pred = [round(value) for value in y_pred]


# Make the Confusion Matrix

from sklearn.metrics import confusion_matrix

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)


# More examples see this: https://xgboost.readthedocs.io/en/latest/get_started.html

