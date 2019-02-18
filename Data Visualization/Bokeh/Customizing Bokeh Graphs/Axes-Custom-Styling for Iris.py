"""
Created on Sun Feb  3 2019

@author: Nodar Okroshiashvili
"""


#Plotting flower species


# Modifies axis of a graph


#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()



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

#Save and show the figure
show(f)



