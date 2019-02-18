"""
Created on Mon Feb  4 20:34:55 2019

@author: Nodar Okroshiashvili

"""


#Plotting periodic table elements




#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet
import pandas
from numpy import nan

# Drop missing elements
elements.dropna(inplace=True)

# Add color map
colormap={'gas':'yellow', 'liquid':'orange', 'solid':'red', nan:'grey'}
# Add element color
elements['color'] = [colormap[x] for x in elements['standard state']]
# Add element size
elements['size'] = elements['van der Waals radius'] / 10

# Bokeh ColumnDataSource
gas = ColumnDataSource(elements[elements['standard state']=='gas'])
liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
solid = ColumnDataSource(elements[elements['standard state']=='solid'])


#Define the output file path
output_file("elements.html")

#Create the figure object
f = figure()

# Adding Glyphs
f1 = figure()
f1.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2, color="color", legend='Gas', source=gas)

f2 = figure()
f2.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2, color="color", legend='Liquid', source=liquid)

f3 = figure()
f3.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2, color="color", legend='Solid', source=solid)

# Make Grid Plot
f = gridplot([[f1,f2], [None,f3]])


#Save and show the figure
show(f)

