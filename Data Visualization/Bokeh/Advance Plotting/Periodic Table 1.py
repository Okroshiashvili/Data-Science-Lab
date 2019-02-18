"""
Created on Sun Feb  3 2019

@author: Nodar Okroshiashvili
"""



# Plot Periodic Table of Elements


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet
from bokeh.models.annotations import Span, BoxAnnotation, Label, LabelSet


# Drop the nan values
elements.dropna(inplace=True)

# Create color map
colormap = {'gas':'yellow', 'liquid':'orange', 'solid':'red'}
elements['color'] = [colormap[x] for x in elements['standard state']]
elements['size'] = elements['van der Waals radius'] / 10


# Create three Column Data Sources for elements of unique standard state
gas = ColumnDataSource(elements[elements['standard state']=='gas'])
liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
solid = ColumnDataSource(elements[elements['standard state']=='solid'])


# Path for output file
output_file("elemnts.html")


# Create figure object
f = figure()


# Adding Glyphs

f.circle(x = "atomic radius",
         y = "boiling point",
         size = "size",
         fill_alpha= 0.2,
         color = "color",
         legend = "Gas",
         source=gas)



f.circle(x = "atomic radius",
         y = "boiling point",
         size = "size",
         fill_alpha= 0.2,
         color = "color",
         legend = "Liquid",
         source=liquid)


f.circle(x = "atomic radius",
         y = "boiling point",
         size = "size",
         fill_alpha= 0.2,
         color = "color",
         legend = "Solid",
         source=solid)


# Add axis labels
f.xaxis.axis_label = "Atomic Radius"
f.yaxis.axis_label = "Boiling Point"



# Define average boing temperature for gas, liquid, and solid
gas_average = sum(gas.data['boiling point'])/len(gas.data['boiling point'])
liquid_average = sum(liquid.data['boiling point']) / len(liquid.data['boiling point'])
solid_average = sum(solid.data['boiling point']) / len(solid.data['boiling point'])


# Add boiling average as a span
gas_span = Span(location = gas_average, dimension = 'width',line_color = 'yellow',line_width = 2)

liquid_span = Span(location = liquid_average, dimension = 'width',line_color = 'orange',line_width = 2)

solid_span = Span(location = solid_average, dimension = 'width',line_color = 'red',line_width = 2)


f.add_layout(gas_span)
f.add_layout(liquid_span)
f.add_layout(solid_span)



# Add labels to spans
gas_span_label = Label(x = 80, y = gas_average, text = "Gas average boiling point",
                       render_mode = 'css')


liquid_span_label = Label(x = 80, y = liquid_average, text = "Liquid average boiling point",
                       render_mode = 'css')


solid_span_label = Label(x = 80, y = solid_average, text = "Solid average boiling point",
                       render_mode = 'css')


f.add_layout(gas_span_label)
f.add_layout(liquid_span_label)
f.add_layout(solid_span_label)



# Show the graph
show(f)

