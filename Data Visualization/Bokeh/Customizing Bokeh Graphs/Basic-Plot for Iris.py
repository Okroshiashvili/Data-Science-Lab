"""
Created on Sun Feb  3 2019

@author: Nodar Okroshiashvili
"""



#Plotting flower species



#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
# DataFrame object
from bokeh.sampledata.iris import flowers


#Define the output file path
output_file("iris.html")

#Create the figure object
f = figure()

#adding glyphs
f.circle(x=flowers["petal_length"], y=flowers["petal_width"])

#Save and show the figure
show(f)


