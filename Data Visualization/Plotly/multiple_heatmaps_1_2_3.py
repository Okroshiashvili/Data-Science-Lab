"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""



import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd


# Read the data
df_1 = pd.read_csv('../data/2010SitkaAK.csv')
df_2 = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df_3 = pd.read_csv('../data/2010YumaAZ.csv')


# Create the traces
trace_1 = go.Heatmap(x = df_1['DAY'],
                     y = df_1['LST_TIME'],
                     z = df_1['T_HR_AVG'],
                     colorscale = 'Jet',
                     zmin = 5, zmax = 40,
                     name = 'Sitka') # Add max/min color values to make
                                          # each plot consistent


trace_2 = go.Heatmap(x = df_2['DAY'],
                     y = df_2['LST_TIME'],
                     z = df_2['T_HR_AVG'],
                     colorscale = 'Jet',
                     zmin = 5, zmax = 40,
                     name = 'Santa Barbara')


trace_3 = go.Heatmap(x = df_3['DAY'],
                     y = df_3['LST_TIME'],
                     z = df_3['T_HR_AVG'],
                     colorscale = 'Jet',
                     zmin = 5, zmax = 40,
                     name = 'Yuma')



# Figure object
fig = tools.make_subplots(rows=1, cols=3,
                          subplot_titles = ('Sitka, AK','Santa Barbara, CA', 'Yuma, AZ'),
                          shared_yaxes=True)

# Append figure with traces
fig.append_trace(trace_1, 1,1)
fig.append_trace(trace_2, 1,2)
fig.append_trace(trace_3, 1,3)


# Update the layout
fig['layout'].update(title = 'Hourly Temperature')



# Plot figure
pyo.plot(fig, filename='multiple_heatmaps.html')


