"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd


# Read the data
df = pd.read_csv('data/iris.csv')


# Create the traces
trace_0 = df[df['class'] == 'Iris-setosa']['petal_length']
trace_1 = df[df['class'] == 'Iris-versicolor']['petal_length']
trace_2 = df[df['class'] == 'Iris-virginica']['petal_length']


# Data variable
hist_data = [trace_0, trace_1, trace_2]


# Group labels
group_labels = ['Iris Setosa', 'Iris Versicolor' ,'Iris Virginica']


# Figure object
fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)

# Plot figure
pyo.plot(fig, filename='iris_displot.html')


