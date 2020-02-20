


"""
Configure graph legends
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
f.tools = [PanTool(), ResetTool()]
f.add_tools(HoverTool())
f.toolbar_location = 'above'
f.toolbar.logo = None



# Style the grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha = 0.6
f.grid.grid_line_dash = [5,3]

colormap = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
flowers['color'] = [colormap[x] for x in flowers['species']]


# Adding glyphs

# Legend for "Setosa"
f.circle(x=flowers["petal_length"][flowers["species"]=="setosa"],
         y=flowers["petal_width"][flowers["species"]=="setosa"],
         size=flowers['sepal_width'][flowers["species"]=="setosa"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="setosa"],
         line_dash=[5,3],
         legend='Setosa')


# Legend for "Versicolor"
f.circle(x=flowers["petal_length"][flowers["species"]=="versicolor"],
         y=flowers["petal_width"][flowers["species"]=="versicolor"],
         size=flowers['sepal_width'][flowers["species"]=="versicolor"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="versicolor"],
         line_dash=[5,3],
         legend='Versicolor')


# Legend for "Virginica"
f.circle(x=flowers["petal_length"][flowers["species"]=="virginica"],
         y=flowers["petal_width"][flowers["species"]=="virginica"],
         size=flowers['sepal_width'][flowers["species"]=="virginica"]*4,
         fill_alpha=0.2,
         color=flowers['color'][flowers["species"]=="virginica"],
         line_dash=[5,3],
         legend='Virginica')



#Save and show the figure
show(f)



