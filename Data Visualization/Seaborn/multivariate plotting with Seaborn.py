"""
Created on Sat May 18 2019

@author: Nodar Okroshiashvili
"""



"""
Data Link:
    https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset

"""




import pandas as pd
import numpy as np
import re
import seaborn as sns
pd.set_option('max_columns',None)



footballers = pd.read_csv('CompleteDataset.csv', index_col=0)



# Some data pre-processing steps.

df = footballers.copy()

df['Unit'] = footballers['Value'].str[-1]

df['Value (M)'] = np.where(df['Unit'] == '0',0,
                           df['Value'].str[1:-1].replace(r'[a-zA-Z]',''))


df['Value (M)'] = df['Value (M)'].astype(float)


df['Value (M)'] = np.where(df['Unit'] == 'M',
                           df['Value (M)'],
                           df['Value (M)']/1000)



df = df.assign(Value=df['Value (M)'],
               position=df['Preferred Positions'].str.split().str[0])



"""
A visual variable is any visual dimension or marker that we can use to
perceptually distinguish two data elements from one another.
Examples include size, color, shape, and one, two, and even three dimensional position.

"""



###       Multivariate Scatter Plot       ###



# See, which type of offensive players tends to get paid the most:
# the striker, the right-winger, or the left-winger

sns.lmplot(x='Value', y='Overall', hue='position',
           data=df.loc[df['position'].isin(['ST', 'RW', 'LW'])],fit_reg=False)



sns.lmplot(x='Value', y='Overall', markers=['o','x','*'], hue='position',
           data=df.loc[df['position'].isin(['ST','RW','LW'])],fit_reg=False)








###       Grouped Box Plot       ###



f = (df.loc[df['position'].isin(['ST','GK'])].loc[:,['Value','Overall',
                                                     'Aggression','position']])



f = f[f['Overall'] >= 80]

f = f[f['Overall'] < 85]

f['Aggression'] = f['Aggression'].astype(float)


sns.boxplot(x='Overall', y='Aggression', hue='position', data=f)




"""
Another way to plot many dataset features while circumnavigating
this problem is to use summarization.
Summarization is the creation and addition of new variables
by mixing and matching the information provided in the old ones.

"""



###     Heatmap or Correlation plot     ###

f = (df.loc[:,['Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control']]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan).dropna()).corr()



sns.heatmap(f, annot=True)




###       Parallel Coordinates     ###


from pandas.plotting import parallel_coordinates


f = (df.iloc[:, 12:17].loc[df['position'].isin(['ST','GK'])].applymap(
        lambda v: int(v) if str.isdecimal(v) else np.nan).dropna())


f['position'] = df['position']

f = f.sample(200)


parallel_coordinates(f, 'position')






