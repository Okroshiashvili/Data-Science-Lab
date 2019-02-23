"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


#   Line chart of US population



import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read the data
df = pd.read_csv('data/population.csv', index_col=0)


## If you want full dataset, uncomment and use this peace of code
#df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')
#
## Extract desired column
#df2 = df[df['DIVISION'] == '1']
## Set index
#df2.set_index('NAME', inplace=True)
#
## Extract population
#list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
#df2 = df2[list_of_pop_col]
#
#
#data = [go.Scatter(x = df2.columns, y = df2.loc[name],
#                   mode = 'lines', name = name) for name in df2.index]



# Create traces
traces = [go.Scatter(x = df.columns,
                     y = df.loc[name],
                     mode = 'markers+lines',
                     name = name) for name in df.index]


# Create layout
layout = go.Layout(
            title = 'Population Estimates of Six US States')



# Figure object
fig = go.Figure(data = traces, layout=layout)


# Plot the data
pyo.plot(fig, filename='POP.html')



