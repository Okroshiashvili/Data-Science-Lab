


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Read data
df = pd.read_csv('data/2018WinterOlympics.csv')


# Create data for Plotly
data = [go.Bar(x = df['NOC'], # National Olympic Commettee
               y = df['Total'])] # Total medals by country


# Create layout
layout = go.Layout(title = 'Total Medals by Country')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot the data
pyo.plot(fig, filename='bar_chart.html')

