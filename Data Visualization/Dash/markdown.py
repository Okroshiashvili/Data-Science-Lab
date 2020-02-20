


import dash
import dash_core_components as dcc
import dash_html_components as html


# Create application
app = dash.Dash()


# Write some markdown
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.

Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

Markdown includes syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
'''


# Define layout
app.layout = html.Div([
    dcc.Markdown(children=markdown_text)])


# Run the application
if __name__ == '__main__':
    app.run_server()



