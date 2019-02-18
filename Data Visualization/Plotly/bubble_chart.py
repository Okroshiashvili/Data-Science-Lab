"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('../data/mpg.csv')


# Add columns to the DataFrame to convert model year into string and
# then combine it with name so that hover text shows both
df['text1'] = pd.Series(df['model_year'], dtype=str)
df['text2'] = "'"+df['text1']+" "+df['name']


# Create data for Plotly
data = [go.Scatter(x = df['horsepower'], y = df['mpg'],
                   text = df['text2'], # When hover-over displys car name
                   mode = 'markers',
                   marker = dict(size = df['weight']/200,# marker size
                                 color = df['cylinders'], # marker color
                                 showscale = True) # shows scale
                   )]


# Create layout for bubble graph
layout = go.Layout(title = 'Bubble Chart',
                   hovermode = 'closest',
                   xaxis = dict(title = 'Horse Power'),
                   yaxis = dict(title = 'Miles per Galon'))


# Create figure object
fig = go.Figure(data = data, layout = layout)

# Plot figure
pyo.plot(fig, filename = 'bubble_chart.html')


