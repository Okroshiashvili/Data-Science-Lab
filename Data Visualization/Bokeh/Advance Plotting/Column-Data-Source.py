


"""
Plotting flower species
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet

colormap={'setosa':'red','versicolor':'green','virginica':'blue'}
flowers['color'] = [colormap[x] for x in flowers['species']]
flowers['size'] = flowers['sepal_width'] * 4


# Create Bokeh ColumnDataSource

# We need three ColumnDataSource for each glyphs
setosa = ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor = ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica = ColumnDataSource(flowers[flowers["species"]=="virginica"])


#Define the output file path
output_file("iris.html")

#Create the figure object
f = figure()

# Adding Glyphs
f.circle(x="petal_length",
         y="petal_width",
         size='size',
         fill_alpha=0.2,
         color="color",
         line_dash=[5,3],
         legend='Setosa',
         source=setosa)

f.circle(x="petal_length",
         y="petal_width",
         size='size',
         fill_alpha=0.2,
         color="color",
         line_dash=[5,3],
         legend='Versicolor',
         source=versicolor)

f.circle(x="petal_length",
         y="petal_width",
         size='size',
         fill_alpha=0.2,
         color="color",
         line_dash=[5,3],
         legend='Virginica',
         source=virginica)

#Save and show the figure
show(f)


