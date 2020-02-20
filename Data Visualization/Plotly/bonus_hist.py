


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('data/FremontBridgeBicycles.csv')


# Convert "Date" columns into datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Add column for hour
df['Hour'] = df['Date'].dt.time


# Aggregation
df2 = df.groupby('Hour').sum()



# Create traces

trace_0 = go.Bar(x = df2.index,
                 y = df2['Fremont Bridge West Sidewalk'],
                 name = 'Southbound',
                 width = 1)

trace_1 = go.Bar(x = df2.index,
                 y = df2['Fremont Bridge East Sidewalk'],
                 name = 'Northbound',
                 width = 1)


data = [trace_0, trace_1]


# Create layout
layout = go.Layout(title = 'Fremont Bridge Bicycle Traffic by Hour',
                   barmode = 'stack')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot figure
pyo.plot(fig, filename='fremont_bridge.html')




