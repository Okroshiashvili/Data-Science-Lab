"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""



import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv('data/abalone.csv')


# Data for Plotly
data = [go.Histogram(
    x=df['length'],
    xbins=dict(start=0,end=1,size=.02),)]


# Create layout
layout = go.Layout(
    title="Shell lengths from the Abalone dataset")


# Figure object
fig = go.Figure(data = data, layout = layout)

# Plor figure
pyo.plot(fig, filename='Abalone.html')

