


"""
Making a basic Bokeh line graph
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show

# from bokeh.plotting import figure, output_file, show



# Prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Prepare the output file
output_file("Line.html")

# Create a figure object
f = figure()

# Create line plot
f.line(x,y)
# The line below plots triangles instead of dots
# If you run this whole script you'll get line and triangle plot
# You can change triangle by circle or any other
# See examples here: https://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html
f.triangle(x,y,size=20)

# Write the plot in the figure object
show(f)


