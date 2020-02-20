


"""
Line Chart of Random Data
"""

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Set random seed
np.random.seed(56)


x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)


# Create the traces
trace_0 = go.Scatter(x = x_values, y = y_values + 5,
                   mode = 'markers',
                   name = 'My Markers')


trace_1 = go.Scatter(x = x_values, y = y_values,
                     mode = 'lines',
                     name = 'My Lines')



trace_2 = go.Scatter(x = x_values, y = y_values - 5,
                     mode = 'lines+markers',
                     name = 'My Lines and Markers')


# Put data in a list
data = [trace_0, trace_1, trace_2]

# Create layout
layout = go.Layout(title = 'Three Different Line Chart')

# Figure object
fig = go.Figure(data = data, layout = layout)


# Plot data
pyo.plot(fig, filename='line charts.html')

