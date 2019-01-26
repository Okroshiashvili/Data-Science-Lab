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
from xgboost import XGBClassifier

# create class object
classifier = xgb.sklearn.XGBClassifier()


# Fit the object to the dataset
classifier.fit(X_train, y_train)


#%%

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#%%

# Make the Confusion Matrix

from sklearn.metrics import confusion_matrix

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

#%%

"""
Applying K-Fold Cross Validation

"""

from sklearn.model_selection import cross_val_score


# We define accuracy vector which will be populated after K-Fold
accuracies = cross_val_score(estimator=classifier, X = X_train, y = y_train, cv = 10)

# Get average accuracy
mean = accuracies.mean()
# Get standard deviation
std = accuracies.std()

#%%
