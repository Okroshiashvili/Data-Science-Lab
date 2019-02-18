"""
Created on Sun Feb  3 16:42:48 2019

@author: Nodar Okroshiashvili
"""



# Full code for Iris dataset





#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
# DataFrame object
from bokeh.sampledata.iris import flowers
# Import for bokeh tools
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool


#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()


# Style the tools

f.tools = [PanTool(),ResetTool()]
hover = HoverTool(tooltips=[("Species","@species"), ("Sepal Width","@sepal_width")])
f.add_tools(hover)
# Define tools location
f.toolbar_location = 'above'
# Logo for tool. "None" removes bokeh icon
f.toolbar.logo = None



#Style the plot area

# Sets background width to 1100 pixels
# Height to 650 pixels
# Background color is "olive"
# Background fill or color intensity or transparancy is 0.3
f.plot_width=1100
f.plot_height=650
f.background_fill_color="olive"
f.background_fill_alpha=0.3



#Style the title

# Sets the title
f.title.text="Iris Morphology"
# Change the title color
f.title.text_color="olive"
# Change the font of title
f.title.text_font="times"
# Set the font size
f.title.text_font_size="25px"
# Title alingment
f.title.align="center"



#Style the axes

# Set color for minor tick on x axis
f.xaxis.minor_tick_line_color="blue"
# f.xaxis.minor_tick_line_color="blue" This command removes minot ticks
# Set label orientation on y axis
f.yaxis.major_label_orientation="vertical"
# x axis will be visible
f.xaxis.visible=True
# Set size for minor ticks
f.xaxis.minor_tick_in=-6
# x axis label
f.xaxis.axis_label="Petal Length"
# y axis label
f.yaxis.axis_label="Petal Width"
# x axis label color
f.axis.axis_label_text_color="blue"
# axis major ticks color
f.axis.major_label_text_color="orange"



#Axes geometry

# Set range for x axis
f.x_range = Range1d(start=0, end=10)
# Set range for y axis
f.y_range = Range1d(start=0, end=5)
# Restricts range of x axis to the range 2 to 6
f.xaxis.bounds = (0, 10)
# Disered number of tick on the x axis
f.xaxis[0].ticker.desired_num_ticks = 2
# Disered number of tick on the y axis
f.yaxis[0].ticker.desired_num_ticks = 2
# Number of ticks between major ticks on x axis
f.xaxis[0].ticker.num_minor_ticks = 10
# Number of ticks between major ticks on y axis
f.yaxis[0].ticker.num_minor_ticks = 10



#Style the grid

# Sets grid line color for vertical lines
# "None" removes the vertical line
f.xgrid.grid_line_color = None
# Set grid line transparancy for horizontal line
f.ygrid.grid_line_alpha = 0.6
# Set grid line to be dashed line 5 by 3 pixels empty box
f.grid.grid_line_dash = [5,3]



# Set the color for each species
colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
# Create column of colors in df
flowers['color']=[colormap[x] for x in flowers['species']]




# Adding Glyphs

# Legend for "Setosa"
f.circle(x=flowers["petal_length"][flowers["species"]=="setosa"],
         y=flowers["petal_width"][flowers["species"]=="setosa"],
         size=flowers['sepal_width'][flowers["species"]=="setosa"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="setosa"],
         line_dash=[5,3],
         legend='Setosa')


# Legend for "Versicolor"
f.circle(x=flowers["petal_length"][flowers["species"]=="versicolor"],
         y=flowers["petal_width"][flowers["species"]=="versicolor"],
         size=flowers['sepal_width'][flowers["species"]=="versicolor"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="versicolor"],
         line_dash=[5,3],
         legend='Versicolor')


# Legend for "Virginica"
f.circle(x=flowers["petal_length"][flowers["species"]=="virginica"],
         y=flowers["petal_width"][flowers["species"]=="virginica"],
         size=flowers['sepal_width'][flowers["species"]=="virginica"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="virginica"],
         line_dash=[5,3],
         legend='Virginica')



#Style the legend

# Set the legend location on the graph
#f.legend.location = (575,555) # pixel coordinates
# Same as above
f.legend.location = 'top_left'
# Background transparancy of legend
f.legend.background_fill_alpha = 0
# Legend border line color
f.legend.border_line_color = None
# Legend margin
f.legend.margin = 10
# Legend padding
f.legend.padding = 18
# Legend text color
f.legend.label_text_color = 'olive'
# Legend text font family
f.legend.label_text_font = 'times'



#Save and show the figure
show(f)


