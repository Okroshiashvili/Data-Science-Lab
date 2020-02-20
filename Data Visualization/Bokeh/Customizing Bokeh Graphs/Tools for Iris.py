


"""
Create extra tools for a graph
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

# Define the output file path
output_file("iris.html")

# reate the figure object
f = figure()

# Style the tools

# Sets only "PanToll" and "ResetTool"
f.tools = [PanTool(),ResetTool()]
# Add extra tool
f.add_tools(HoverTool())
# Define tools location
f.toolbar_location = 'above'
# Logo for tool. "None" removes bokeh icon
f.toolbar.logo = None



#Save and show the figure
show(f)


