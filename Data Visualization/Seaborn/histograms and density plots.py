"""
Created on Thu May 16 2019

@author: Nodar Okroshiashvili
""""




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



iris_data = pd.read_csv('data/iris.csv', index_col='Id')



# Histogram
sns.distplot(a = iris_data['Petal Length (cm)'], kde=False)



# Kernel Density Estimate (kde)
# This is the smoothed histogram

# kde plot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)


# We can create two-dimensional kde plot
sns.jointplot(x=iris_data['Petal Length (cm)'],
              y=iris_data['Sepal Width (cm)'], kind='kde')








# Let split the data to understand difference btw species

iris_set_data = pd.read_csv('data/iris_setosa.csv', index_col="Id")
iris_ver_data = pd.read_csv('data/iris_versicolor.csv', index_col="Id")
iris_vir_data = pd.read_csv('data/iris_virginica.csv', index_col="Id")


# Plot three histogram for each species
sns.distplot(a=iris_set_data['Petal Length (cm)'],
             label="Iris-setosa", kde=False)

sns.distplot(a=iris_ver_data['Petal Length (cm)'],
             label="Iris-versicolor", kde=False)

sns.distplot(a=iris_vir_data['Petal Length (cm)'],
             label="Iris-virginica", kde=False)

plt.title("Histogram of Petal Lengths, by Species")
plt.legend()




# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'],
            label="Iris-setosa", shade=True)

sns.kdeplot(data=iris_ver_data['Petal Length (cm)'],
            label="Iris-versicolor", shade=True)

sns.kdeplot(data=iris_vir_data['Petal Length (cm)'],
            label="Iris-virginica", shade=True)

plt.title("Distribution of Petal Lengths, by Species")



