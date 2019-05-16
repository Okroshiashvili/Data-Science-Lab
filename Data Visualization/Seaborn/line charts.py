"""
Created on Thu May 16 2019

@author: Nodar Okroshiashvili
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


spotify = pd.read_csv('data/spotify.csv', index_col='Date', parse_dates=True)


# Line Plot
sns.lineplot(data=spotify)


# Customize the plot
plt.figure(figsize=(10,6))
plt.title('Daily Global Streams of Popular Songs in 2017-2018')
sns.lineplot(data=spotify)




# Plot Subset of data
plt.figure(figsize=(10,6))
plt.title('Daily Global Streams of Popular Songs in 2017-2018')
sns.lineplot(data = spotify['Shape of You'], label = 'Shepe of You')
sns.lineplot(data = spotify['Despacito'], label = 'Despacito')
plt.xlabel('Date')





