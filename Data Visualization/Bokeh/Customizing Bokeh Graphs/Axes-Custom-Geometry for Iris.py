


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("iris.html")

#Create the figure object
f = figure()


#Axes geometry

# Set range for x axis
f.x_range = Range1d(start=0, end=10)
# Set range for y axis
f.y_range = Range1d(start=0, end=5)
# Restricts range of x axis to the range 2 to 6
f.xaxis.bounds = (2, 6)
# Disered number of tick on the x axis
f.xaxis[0].ticker.desired_num_ticks = 2
# Disered number of tick on the y axis
f.yaxis[0].ticker.desired_num_ticks = 2
# Number of ticks between major ticks on y axis
f.yaxis[0].ticker.num_minor_ticks = 10

#Save and show the figure
show(f)


