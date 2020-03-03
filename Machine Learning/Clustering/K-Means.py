


"""
K-Means

"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans

# Import the dataset
dataset = pd.read_csv('data/Mall_Customers.csv')


# Create independent variable
X = dataset.iloc[:, [3,4]].values



# Using the Elbow Method to find the optimal number of clusters
# We have to write for loop, to loop inside ten clusters and plot the result

# create empty list
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    # we create k-means object we some parameters
    # n_cluster is the number of cluster or our iterator
    # init is to avoid random initialization trap
    # max_iter means maximum number of iterations to find final clusters
    # n_init is number of times the algorithm, will be run with different initial centroids
    kmeans.fit(X)
# Fit the model to the dataset
    wcss.append(kmeans.inertia_)
# computes wcss or inertia


# Plot the result of loop
# The plot show that 5 cluster will be optimal
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()



# Now let apply k-means to the dataset


# Create new k-means object
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter=300, n_init=10, random_state=0)


# Make "prediction" which client belongs to which cluster
y_kmeans = kmeans.fit_predict(X)



# Visualize the clusters along with data points

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Careful')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Target')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100, c='magenta', label='Sensible')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()

