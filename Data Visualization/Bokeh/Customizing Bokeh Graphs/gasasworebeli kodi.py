#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:07:45 2019

@author: nodo
"""

#Plotting flower species
 
#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, WheelZoomTool
from screeninfo import get_monitors
 
#Define the output file path
output_file("iris.html")
 
#Create the figure object
f = figure(tools=[PanTool(), ResetTool(), WheelZoomTool()])
 
#Style the tools
hover = HoverTool(tooltips=[("Species","@species"), ("Sepal Width", "@sepal_width")])
f.add_tools(hover)
f.toolbar_location = 'above'
f.toolbar.logo = None
 
#Style the plot area
f.plot_width=get_monitors()[0].width #get_monitors is part of the screeninfo module imported above
f.plot_height=get_monitors()[0].height-50 #get_monitors is part of the screeninfo module imported above
f.background_fill_color = "grey"
f.background_fill_alpha = 0.1
f.sizing_mode = "stretch_both" #graph will resize itself when user resizes the browser
 
#Style the title
f.title.text = "Iris Morphology"
f.title.text_color = "olive"
f.title.text_alpha = 0.6
f.title.text_font = "antiqua"
f.title.text_font_size = "18px"
f.title.align = "center"
 
#Style the axes
f.yaxis.major_label_orientation = "vertical"
f.xaxis.minor_tick_in = -6
f.yaxis.minor_tick_in = -6
f.axis.minor_tick_line_color = "grey"
f.axis.axis_line_color = "olive"
f.xaxis.axis_label = "Petal Length"
f.yaxis.axis_label = "Petal Width"
f.axis.axis_label_text_color = "olive"
f.axis.axis_label_text_font = "antiqua"
f.axis.axis_label_text_font_style = "bold"
f.axis.major_label_text_color = "olive"
 
#Axes geometry
f.x_range = Range1d(start=flowers["petal_length"][flowers["species"]=='versicolor'].min(),
end=flowers["petal_length"][flowers["species"]=='versicolor'].max())
f.y_range = Range1d(start=flowers["petal_width"][flowers["species"]=='versicolor'].min(),
end=flowers["petal_width"][flowers["species"]=='versicolor'].max())
f.xaxis[0].ticker.desired_num_ticks = 6
f.yaxis[0].ticker.desired_num_ticks = 6
f.yaxis[0].ticker.num_minor_ticks = 5
f.xaxis[0].ticker.num_minor_ticks = 5
 
#Style the grid
f.grid.grid_line_color = (128,128,0,0.5) #equivalent to olive color with a 0.5 alpha value
f.grid.grid_line_dash = [5,3] #5 pixels of line and 3 pixels of space
f.grid.minor_grid_line_color = (128,128,0,0.1) #equivalent to olive color with a 0.1 alpha value
f.grid.minor_grid_line_dash = [3,3]
 
colormap = {'setosa':'red','versicolor':'green','virginica':'blue'}
flowers['color'] = [colormap[x] for x in flowers['species']]
 
#adding glyphs
f.circle(x=flowers["petal_length"][flowers["species"]=="setosa"],
y=flowers["petal_width"][flowers["species"]=="setosa"],
size=flowers['sepal_width'][flowers["species"]=="setosa"]*4,
fill_alpha=0.2, color=flowers['color'][flowers["species"]=="setosa"],
line_dash=[5,3], legend='Setosa')
 
f.circle(x=flowers["petal_length"][flowers["species"]=="versicolor"],
y=flowers["petal_width"][flowers["species"]=="versicolor"],
size=flowers['sepal_width'][flowers["species"]=="versicolor"]*4,
fill_alpha=0.2, color=flowers['color'][flowers["species"]=="versicolor"],
line_dash=[5,3], legend='Versicolor')
 
f.circle(x=flowers["petal_length"][flowers["species"]=="virginica"],
y=flowers["petal_width"][flowers["species"]=="virginica"],
size=flowers['sepal_width'][flowers["species"]=="virginica"]*4,
fill_alpha=0.2, color=flowers['color'][flowers["species"]=="virginica"],
line_dash=[5,3], legend='Virginica')
 
#Style the legend
f.legend.location = "top_left"
f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.spacing = 1
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'antiqua'
 
#Save and show the figure
show(f)