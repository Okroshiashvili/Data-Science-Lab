


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('data/mpg.csv')


# Data for Plotly
data = [go.Histogram(x = df['mpg'])] # Plotly's default bin size seems reasonable



# Create layout
layout = go.Layout(title = 'Miles per Gallon Frequencies of<br>\
                   1970\'s Era Vehicles')


# Figure object
fig = go.Figure(data = data, layout = layout)


# Plot the figure
pyo.plot(fig, filename = 'histogram.html')

