


from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout




# Create widgets
text_input = TextInput(value="Nodar")
button = Button(label="Generate Text")
output = Paragraph()

def update():
    output.text = "Hello, " + text_input.value
    
button.on_click(update)

lay_out = layout([[button, text_input],[output]])



curdoc().add_root(lay_out)


