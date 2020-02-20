


import dash
import dash_html_components as html


# Dash application
app = dash.Dash()


# Dash layout
app.layout = html.Div([
        'This is the outermost div',
        # Add another div
        html.Div(['This is inner Div'],
                 # Style dictionary for inner div
                 style = {'color':'red',
                          'border':'2px red solid',
                          'borderRadius':5,
                          'padding':10,
                          'width':220}),
                 # Add another div element
        html.Div(['Another inner div'],
                 # Add style dict for another div
                 style = {'color':'blue',
                          'border':'3px blue solid',
                          'margin':10,
                          'width':220})
                 ],
         # Add style dictionary for outermost Div
         style = {'width':500,
                  'height':200,
                  'color':'green',
                  'border':'2px green dotted'})


# Run the application
if __name__ == '__main__':
    app.run_server()




