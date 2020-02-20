


"""
In this example I present how to return multiple outputs.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


# Read the data
df = pd.read_csv('data/wheels.csv')


# Create app
app = dash.Dash()


# Create layout for app
app.layout = html.Div([
        dcc.RadioItems(
                id = 'wheels',
                options = [{'label':i, 'value':i} for i in df['wheels'].unique()],
                value = 1),
        html.Div(id = 'wheels-output'),
        
        html.Hr(), # Add horizontal rule for nice separate
        
        dcc.RadioItems(
                id = 'colors',
                options = [{'label':i, 'value':i} for i in df['color'].unique()],
                value = 'blue'
                ),
            html.Div(id = 'colors-output')
        ], style = {'fontFamily': 'Helvetica', 'fontSize':18})
        
        


# Create two functions. One for a wheel and one for a color



@app.callback(Output('wheels-output', 'children'),
              [Input('wheels', 'value')])
# Function for the wheels
def callback_a(wheels_value):
    return "You chose {}".format(wheels_value)




@app.callback(Output('colors-output', 'children'),
              [Input('colors', 'value')])
# Function for the colors
def callback_b(colors_value):
    return "You select {}".format(colors_value)




# Run the app
if __name__ == '__main__':
    app.run_server()

