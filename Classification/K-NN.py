"""
Created on Mon Feb  5 15:39:45 2018

@author: Nodar.Okroshiashvili

"""
#%%

"""
K Nearest Neighbors

"""

#%%

# Pre-processing of data


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%


# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')

# Independent variables
X = dataset.iloc[:, [2,3]].values

# Dependent variable
y = dataset.iloc[:, 4].values

#%%

from sklearn.cross_validation import train_test_split


# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


#%%

# Feature Scaling
from sklearn.preprocessing import StandardScaler

# Define scaler object
sc_X = StandardScaler()

# Apply scaler object to the train and test set
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#%%

# Fitting KNN to the Training set
from sklearn.neighbors import KNeighborsClassifier

# Define classifier object
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)

# Fit the model
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

# Visualizing the Training set results

from matplotlib.colors import ListedColormap

# Re-define variables
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red','green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN Classifier (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#%%

# Visualizing the Test set results

from matplotlib.colors import ListedColormap

# Re-define variables
X_set, y_set = X_test, y_test

X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red','green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


