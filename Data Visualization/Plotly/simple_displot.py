"""
Created on Sat Feb 16 2019

@author: Nodar Okroshiashvili
"""


import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np


# Data set up
x = np.random.randn(1000)

# Data for histogram part for distribution plot
hist_data = [x]

# Group labels
group_labels = ['displot']

# Figure object
fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)

# Plot figure
pyo.plot(fig, filename='simple_displot.html')



