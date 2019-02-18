"""
Created on Sun Feb  3 2019

@author: Nodar Okroshiashvili
"""



# Plot Periodic Table of Elements


from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet
from bokeh.models.annotations import Span, BoxAnnotation, Label, LabelSet
from bokeh.layouts import layout
from bokeh.models.widgets import Select

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
solid_min = min(solid.data['boiling point'])
solid_max = max(solid.data['boiling point'])

# Add boiling average as a span
gas_span = Span(location = gas_average, dimension = 'width',line_color = 'yellow',line_width = 2)

liquid_span = Span(location = liquid_average, dimension = 'width',line_color = 'orange',line_width = 2)

solid_span = Span(location = solid_average, dimension = 'width',line_color = 'red',line_width = 2)


f.add_layout(gas_span)
f.add_layout(liquid_span)
f.add_layout(solid_span)



#Create a function that updates the location attribute value for span_solid_boil span
#Also note that select.value returns values as strings
# so we need to convert the returned value to float
def update_span(attr, old, new):
    solid_span.location = float(select.value)
    
  
    
# Select widgets expect a list of tuples of strings,
# so List[Tuple(String, String)], that's why you should convert average,
# max, and min to strings

options = [(str(solid_average),"Solid Average Boiling Point"),
           (str(solid_min), "Solid Min Boiling Point"),
           (str(solid_max),"Solid Max Boiling Point")]

# Create the select widget
select = Select(title = "Select span value", options=options)
select.on_change("value", update_span)


# Add select widget to layout    
lay_out = layout([[select]])

# Add layout to curdoc
curdoc().add_root(f)
curdoc().add_root(lay_out)
    
