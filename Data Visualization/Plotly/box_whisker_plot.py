


import plotly.offline as pyo
import plotly.graph_objs as go


# Setup data
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]



# Data for Plotly
data = [go.Box(y = y,
               boxpoints = 'all', # shows all data points
               # to show outliers only set: boxpoints = 'outliers'
               jitter = 0.3, # little noise to spred out the existing points
               pointpos = 0, # offset points left or right or center
               )]

# Plot the data
pyo.plot(data, filename = 'box_plot.html')


