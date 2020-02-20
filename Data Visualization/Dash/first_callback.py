


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Create app
app = dash.Dash()


# Adjust application layout
app.layout = html.Div([
        # Dash core component
        dcc.Input(id = 'my-id', value = 'Initial Text', type = 'text'),
        # html component
        html.Div(id = 'my-div')
])



# Connect components by using callback
@app.callback(Output(component_id='my-div', component_property='children'),
              [Input(component_id='my-id', component_property='value')])

def update_output_div(input_value):
    return "You entered: {}".format(input_value)

# We are going to connect text entered in Dash core component
# to be displayed in html Div tag. To do that we have to use decorator
    



# Run the app
if __name__ == '__main__':
    app.run_server()


