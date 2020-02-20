


"""
Making a basic Bokeh line graph
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


# Prepare some data

# df is Pandas DataFrame
df = pandas.read_csv("data/data.csv")
# x and y are Pandas Series
x = df["x"]
y = df["y"]

# Prepare the output file
output_file("Line_from_csv.html")

# Create a figure object
f = figure()

# Create line plot
f.line(x,y)

# Write the plot in the figure object
show(f)


