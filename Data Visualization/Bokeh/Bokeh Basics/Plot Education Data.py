


import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show


# Read Data
df = pd.read_csv('data/bachelors.csv')

x = df['Year']
y = df['Engineering']


# Output File
output_file("Edu Data.html")


# Create Figure Object
f = figure()


# Line Plot
f.line(x,y)
f.circle(x,y, size=8)


# Show Plot
show(f)


