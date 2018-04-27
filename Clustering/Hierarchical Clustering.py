"""
Created on Sun Feb 25 12:49:12 2018

@author: Nodar.Okroshiashvili
"""
#%%

"""

Hierarchical Clustering

"""

#%%

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the dataset
dataset = pd.read_csv('data/Mall_Customers.csv')


# Create independent variable
X = dataset.iloc[:, [3,4]].values

#%%

# Using the dendrogram to find optimal number of clusters

import scipy.cluster.hierarchy as sch

dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
# "ward" method tries to minimize variance within each cluster
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

#%%

# Fitting HC to the dataset

from sklearn.cluster import AgglomerativeClustering


# Create clustering object
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')


# Make "prediction" which client belongs to which cluster
y_hc = hc.fit_predict(X)

#%%

# Visualize the clusters along with data points

plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c='red', label='Careful')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c='green', label='Target')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s=100, c='magenta', label='Sensible')
plt.title('Clusters of clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()

#%%
