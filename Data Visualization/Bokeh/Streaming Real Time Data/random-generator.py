"""
Created on Sat Feb  9 2019

@author: Nodar Okroshiashvili
"""


#      Serve Random Number Generation in Bokeh Server



#import libraries
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

# Create Figure
f = figure(x_range=(0,11),y_range=(0,11)) # Set range for axes

# Create ColumnDataSource
source=ColumnDataSource(data=dict(x=[],y=[]))

# Create Glyphs
f.circle(x='x',
         y='y',
         size=10,
         fill_color='olive',
         line_color='brown',
         source=source)

f.line(x='x', y='y', source=source)


# Create Periodic Function
def update():
    new_data=dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=20)
    #print(source.data)

# Add figure to curdoc
curdoc().add_root(f)
# Configure callback
curdoc().add_periodic_callback(update,1000) # callback every 1000 mili second


