


"""
Glyphs are the elements on the graph
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

# Define the output file path
output_file("iris.html")

# Create the figure object
f = figure()

# Style the tools
f.tools = [PanTool(),ResetTool()]
f.add_tools(HoverTool())
f.toolbar_location = 'above'
f.toolbar.logo = None



# Style the grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha = 0.6
f.grid.grid_line_dash = [5,3]

# Set the color for each species
colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
# Create column of colors in df
flowers['color']=[colormap[x] for x in flowers['species']]

# adding glyphs
f.circle(x=flowers["petal_length"], y=flowers["petal_width"],
         size=flowers['sepal_width']*4,
         fill_alpha=0.2, color=flowers['color'], line_dash=[5,3])

# Save and show the figure
show(f)


