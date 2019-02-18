"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


#    Scatter Plot



import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# Set seed
np.random.seed(42)

# Draw random integers
rand_x = np.random.randint(1,101,100)
rand_y = np.random.randint(1,101,100)

# Create data object
data = [go.Scatter(
        x = rand_x,
        y = rand_y,
        mode = 'markers',
        # Change marker tyle
        marker = dict(size = 12,
                      color = 'rgb(27,04,92)',
                      symbol = 'square',
                      line = dict(width = 2,)
                      ))]

# Layout object
layout = go.Layout(
            title = 'Scatter of Random Data', # Title of the Scatter
            xaxis = dict(title = 'Random X Values'), # X axis label
            yaxis = dict(title = 'Random Y Values'), # Y axis label
            hovermode = 'closest') # Handles multiple points on the same vertical

# Figure object
fig = go.Figure(data=data, layout=layout)

# Plot figure object
pyo.plot(fig, filename="sctter.html")



