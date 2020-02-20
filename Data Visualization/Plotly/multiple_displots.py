


import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np



# Data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4


# Data for histogram part
hist_data = [x1, x2, x3, x4]

# Group labels
group_labels = ['X1', 'X2', 'X3', 'X4']


# Figure object
fig = ff.create_distplot(hist_data=hist_data,
                         group_labels=group_labels,
                         bin_size=[.2, .1, .3, .4])

# Plot figure
pyo.plot(fig, filename = 'multiple_displot.html')


