


"""
Set Grid for Iris graph
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

# Define the output file path
output_file("iris.html")

# Create the figure object
f = figure()


# Style the grid

# Sets grid line color for vertical lines
# "None" removes the vertical line
f.xgrid.grid_line_color = None
# Set grid line transparancy for horizontal line
f.ygrid.grid_line_alpha = 0.9
# Set grid line to be dashed line 5 by 3 pixels empty box
f.grid.grid_line_dash = [5,3]

# Save and show the figure
show(f)


