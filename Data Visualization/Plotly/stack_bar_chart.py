"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Read data
df = pd.read_csv('../data/2018WinterOlympics.csv')


# Create traces

trace_0 = go.Bar(x = df['NOC'],# National Olympic Commettee
                 y = df['Gold'],
                 name = 'Gold',
                 marker = {'color':'#FFD700'})


trace_1 = go.Bar(x = df['NOC'],
                 y = df['Silver'],
                 name = 'Silver',
                 marker = {'color':'#9EA0A1'})



trace_2 = go.Bar(x = df['NOC'],
                 y = df['Bronze'],
                 name = 'Bronze',
                 marker = {'color':'#CD7F32'})


data = [trace_0, trace_1, trace_2]


# Create layout
layout = go.Layout(title = 'Total Medals by Country and by Medal Type',
                   barmode = 'stack')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot the data
pyo.plot(fig, filename='stack_bar_chart.html')
