


"""

Customize only Background

"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers

# Define the output file path
output_file("iris.html")

# Create the figure object
f=figure()


# Style the plot area

# Sets background width to 1100 pixels
# Height to 650 pixels
# Background color is "olive"
# Background fill or color intensity or transparency is 0.3
f.plot_width=1100
f.plot_height=650
f.background_fill_color="olive"
f.background_fill_alpha=0.3

#Save and show the figure
show(f)

