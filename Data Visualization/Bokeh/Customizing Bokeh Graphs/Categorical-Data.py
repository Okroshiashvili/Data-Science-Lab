


"""
How to deal with Categorical axes
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare the output
output_file("students.html")

# create the figure
# Set the axes
f = figure(x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
           y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"])

# create glyphs
f.circle(x=["A","B"], y=["C","D"], size=8)

show(f)

