


"""
Bokeh Server
"""


from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.layouts import layout

# Crate ColumnDataDource
source=ColumnDataSource(dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudidn"]))

# Create the figure
f = figure(x_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],
           y_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"])

# Add labels for glyphs
labels=LabelSet(x="average_grades",y="exam_grades",
                text="student_names",x_offset=5,
                y_offset=5,
                source=source)

f.add_layout(labels)

# Create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)


# Create function to update select widget options
def update_labels(attr,old,new):
    labels.text=select.value

# Options for select widget
options=[("average_grades","Average Grades"),
         ("exam_grades","Exam Grades"),
         ("student_names","Student Names")]

# Select widget
select=Select(title="Attribute",options=options)

# Calls function "update_labels" and changes the widget
# sends "value" to the update function
select.on_change("value",update_labels)


# Create layout
lay_out=layout([[select]])

# Add to curdoc
curdoc().add_root(f)
curdoc().add_root(lay_out)


