


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Read the data
df = pd.read_csv('data/mocksurvey.csv', index_col = 0)



# # If you want simple bar chart uncomment this

# # This is for simple bar chart

# # Create trace as a list comprehension
# data = [go.Bar(x = df.index,
#               y = df[response],
#               name = response) for response in df.columns]



# This is for horizontal bar chart
data = [go.Bar(y = df.index, 
               x = df[response], # reverse the axis
               name = response,
               orientation = 'h') for response in df.columns]


# Create layout
layout = go.Layout(title = 'Mock Survey Results',
                   barmode = 'stack')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot the figure
pyo.plot(fig, filename = 'mock_survey.html')

