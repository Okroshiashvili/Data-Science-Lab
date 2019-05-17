"""
Created on Thu May 16 2019

@author: Nodar Okroshiashvili
"""


"""
Data Link:
    https://www.kaggle.com/zynicide/wine-reviews
    
"""





import pandas as pd


df = pd.read_csv('winemag-data_first150k.csv', index_col=0)




###           Bar charts        ###
df['province'].value_counts().head(10).plot.bar(figsize=(10,6))

# Horizontal Bar chart
df['province'].value_counts().head(10).plot.barh(figsize=(10,6))

# If we want to see the relative proportion of wine makers
(df['province'].value_counts().head(10) / len(df)).plot.bar(figsize=(10,6))


# One more Bar chart
df['points'].value_counts().sort_index().plot.bar(figsize=(10,6))




###         Line chart       ###

df['points'].value_counts().sort_index().plot.line(figsize=(10,6))





###         Area chart       ###

df['points'].value_counts().sort_index().plot.area(figsize=(10,6))





###         Histograms       ###

df[df['price'] < 200]['price'].plot.hist(figsize=(10,6))

df['price'].plot.hist(figsize=(10,6))

df['points'].plot.hist(figsize=(10,6))





###         Scatter plot       ###

df[df['price'] < 100].sample(100).plot.scatter(x='price', y='points')
# I downsample the data due to same points overlap and we lose the shape of plot
df[df['price'] < 100].plot.scatter(x='price', y='points')

# To deal with overplotting like this there is another type of plot "Hexplot"





###         Hexplot       ###

df[df['price'] < 100].plot.hexbin(x='price', y='points', gridsize=15)





######         Sub-plots       ######


import matplotlib.pyplot as plt
import seaborn as sns


fig, axarr = plt.subplots(2, 1, figsize=(12, 8))

df['points'].value_counts().sort_index().plot.bar(ax = axarr[0])
df['province'].value_counts().head(20).plot.bar(ax = axarr[1])

# That was 2 by 1 plot. Now let do 2 by 2 plot

fig, axarr = plt.subplots(2, 2, figsize=(12,8))

df['points'].value_counts().sort_index().plot.bar(ax=axarr[0][0], color='green')
axarr[0][0].set_title('Wine Scores')

df['variety'].value_counts().head(20).plot.bar(ax=axarr[1][0], color='green')
axarr[1][0].set_title('Wine Varieties')

df['province'].value_counts().head(20).plot.bar(ax=axarr[1][1], color='green')
axarr[1][1].set_title('Wine Origins')

df['price'].value_counts().plot.hist(ax=axarr[0][1], color='green')
axarr[0][1].set_title('Wine prices')

sns.despine()

