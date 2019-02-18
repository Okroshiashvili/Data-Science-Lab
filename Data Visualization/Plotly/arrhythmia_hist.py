"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


#   Histogram of Arrhythmia dataset

# Compares heights by gender


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('../data/arrhythmia.csv')



# Data object
data = [go.Histogram(x = df[df['Sex'] == 0]['Height'],
                     opacity = 0.75,
                     name = 'Male'),
        go.Histogram(x = df[df['Sex'] == 1]['Height'],
                     opacity = 0.75,
                     name = 'Female'
                     )]


# Create layout
layout = go.Layout(title = 'Height by Gender',
                   barmode = 'overlay',
                   xaxis = dict(title = 'Height'),
                   yaxis = dict(title = 'Frequency'))


# Figure object
fig = go.Figure(data = data, layout = layout)


# Plot figure
pyo.plot(fig, filename = 'arrhythmia_histogram.html')


