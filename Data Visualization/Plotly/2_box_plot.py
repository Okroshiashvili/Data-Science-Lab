


import plotly.offline as pyo
import plotly.graph_objs as go


# Setup data
y = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
x = [.225,.262,.217,.240,.230,.229,.235,.217]



# Data for Plotly
data = [go.Box(y = y, name = 'Snodgrass'),
        go.Box(y = x, name = 'Twain')]


# Create layput
layout = go.Layout(title = 'Two Box and Whisker Plots')

# Create figure object
fig = go.Figure(data = data, layout = layout)


# Plot the data
pyo.plot(fig, filename = '2_box_plot.html')


