#Making a basic Bokeh line graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.resources import CDN



#prepare some data
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output file
#output_file("Line.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

js,div=components(f)

cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]

#write the plot in the figure object
#show(f)
