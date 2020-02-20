


import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Pandas DataFrame
df = pd.read_csv('data/2010YumaAZ.csv')

days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']



# We use for loop to create traces

data = []

for day in days:
    trace = go.Scatter(x = df['LST_TIME'],
                       y = df[df['DAY'] == day]['T_HR_AVG'],
                       mode = 'markers+lines',
                       name = day)
    data.append(trace)


# Create layout
layout = go.Layout(
            title = 'Daily Temperature',
            hovermode = 'closest')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot the data
pyo.plot(fig, filename='temperature.html')

