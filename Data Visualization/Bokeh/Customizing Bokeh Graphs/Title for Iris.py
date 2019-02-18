"""
Created on Sun Feb  3 2019

@author: Nodar Okroshiashvili
"""



#Plotting flower species


# Sets the Title for a graph


#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()



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

#Save and show the figure
show(f)

