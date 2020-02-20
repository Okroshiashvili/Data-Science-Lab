


"""
Plotting flower species
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet

# Define color map
colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
# Add flowers color
flowers['color'] = [colormap[x] for x in flowers['species']]
# dd flowers sepal width multilied by 4
flowers['size'] = flowers['sepal_width'] * 4

# Picture for each flower
urlmap = {'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
        'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
        'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}

# Add flower pictures
flowers['imgs'] = [urlmap[x] for x in flowers['species']]


# Define bokeh column data source
setosa=ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor=ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica=ColumnDataSource(flowers[flowers["species"]=="virginica"])


#Define the output file path
output_file("iris.html")

#Create the figure object
f=figure()

#adding glyphs
f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2,
color = "color", line_dash=[5,3], legend='Setosa', source=setosa)

f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2,
color="color", line_dash=[5,3], legend='Versicolor', source=versicolor)

f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2,
color="color", line_dash=[5,3], legend='Virginica', source=virginica)


# This adds features but I don't like it
labels = LabelSet(x='petal_length', y='petal_width', text='sepal_length', 
level='glyph', x_offset=5, y_offset=5, source=virginica)

f.add_layout(labels)



#Style the tools
f.tools = [PanTool(),ResetTool()]

hover = HoverTool(tooltips="""
     <div>
            <div>
                <img
                    src="@imgs" height="42" alt="@imgs" width="42"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 15px; font-weight: bold;">@species</span>
            </div>
            <div>
                <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
                <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
            </div>
        </div>
""")

f.add_tools(hover)
f.toolbar_location = 'above'
f.toolbar.logo = None


#Style the legend
f.legend.location = (575,555)
f.legend.location = 'top_left'
f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'times'

#Save and show the figure
show(f)
