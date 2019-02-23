"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""



import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('data/2010SitkaAK.csv')


# Data variable
data = [go.Heatmap(x = df['DAY'],
                   y = df['LST_TIME'],
                   z = df['T_HR_AVG'],
                   colorscale = 'Jet'
                   )]



# Create layout
layout = go.Layout(title = 'Hourly Temperature in Sitka, AK')


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plot figure
pyo.plot(fig, filename='heatmap_3.html')


