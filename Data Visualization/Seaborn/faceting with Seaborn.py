


"""
Data Link:

    https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset





Faceting is the act of breaking data variables up across multiple subplots,
and combining those subplots into a single figure. 
   
"""


import pandas as pd
import numpy as np
import re
import seaborn as sns
pd.set_option('max_columns',None)


# Read data
footballers = pd.read_csv('data/CompleteDataset.csv', index_col=0)



### Some data pre-processing steps.

# Make a copy
df = footballers.copy(deep=True)

df['Unit'] = footballers['Value'].str[-1]

df['Value (M)'] = np.where(df['Unit'] == '0',0,
                           df['Value'].str[1:-1].replace(r'[a-zA-Z]',''))


df['Value (M)'] = df['Value (M)'].astype(float)


df['Value (M)'] = np.where(df['Unit'] == 'M',
                           df['Value (M)'],
                           df['Value (M)']/1000)



df = df.assign(Value=df['Value (M)'],
               position=df['Preferred Positions'].str.split().str[0])




###            The FacetGrid           ###


# We're interested in comparing strikers with goalkeepers in some way.

data = df[df['position'].isin(['ST','GK'])]


g = sns.FacetGrid(data, col='position')

# We can use map object to plot the data into laid-out grid

g.map(sns.kdeplot, "Overall")




# FacetGrid for all positions

g = sns.FacetGrid(df, col='position', col_wrap=6)
g.map(sns.kdeplot, 'Overall')




# Suppose we're interested in comparing the talent distribution across rival clubs

data = df[df['position'].isin(['ST', 'GK'])]
data = data[data['Club'].isin(['Real Madrid CF', 'FC Barcelona','Atlético Madrid'])]


g = sns.FacetGrid(df, row='position', col='Club')
g.map(sns.violinplot, 'Overall')



# We can order subplots

g = sns.FacetGrid(df, row='position', col='Club',
                  row_order=['GK', 'ST'],
                  col_order=['Atlético Madrid', 'FC Barcelona', 'Real Madrid CF'])
g.map(sns.violinplot, 'Overall')




###           Pairplot            ###

sns.pairplot(df[['Overall','Potential','Value']])



