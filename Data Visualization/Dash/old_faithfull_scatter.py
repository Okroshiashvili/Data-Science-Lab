# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 2019

@author: Nodar Okroshiashvili
"""



import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd



# Create application
app = dash.Dash()


# Read the data
df = pd.read_csv('data/OldFaithful.csv')

# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).



# Data for Plotly
data = [go.Scatter(
        x = df['X'],
        y = df['Y'],
        mode = 'markers',
        marker = dict(size = 12,
                      color = 'rgb(192,191,4)',
                      symbol = 'circle'))]


# Create layout
layout = go.Layout(title = 'Old Faithfull Eruption Intervals vs Durations',
                   xaxis = dict(title = 'Duration of Eruption (minute)'),
                   yaxis = dict(title = 'Interval to Next Eruption (minute)'),
                   hovermode = 'closest')

# Figure object
fig = go.Figure(data = data, layout = layout)



# Dash layout
app.layout = html.Div([
        dcc.Graph(id = 'old_faithfull',figure = fig)
        ])



# Run the server
if __name__ == '__main__':
    app.run_server()


"""

The scatter plot shows that as geyser eruption duration lasts longer then
the interval increases between eruption. For example if one eruption has
duration 5 minute then the next eruption will occure after 75 minute
