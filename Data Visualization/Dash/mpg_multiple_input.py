# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 2019

@author: Nodar Okroshiashvili
"""




"""

Input parameters are passed to the callback decorator as a list. For this
reason we can include multiple inputs in our dashboard to affect the same
output through the callback functio. 

In this example I put two input components - both dropdowns

"""





import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd



# Read the data
df = pd.read_csv('data/mpg.csv')


# Create the app
app = dash.Dash()


# Extract features names from DataFrame
features = df.columns


# Create the layout
app.layout = html.Div([
        # First Div tag
        html.Div([
                dcc.Dropdown(id='xaxis',
                            options = [{'label': i.title(), 'value':i} for i in features],
                            # Set initial value for dropdown
                            value = 'displacement')
                # Style parameters for first Div
                ],style = dict(width = '40%', display = 'inline-block')),
        # Second Div tag
        html.Div([
                dcc.Dropdown(id='yaxis',
                              options = [{'label': i.title(), 'value':i} for i in features],
                              # Set the initial value for second dropdown
                              value = 'mpg')
                # Style parameters for second Div
                ],style = dict(width = '40%', display = 'inline-block')),
        # Graph object
        dcc.Graph(id = 'feature-graphic')
        ],# Style outmost Div tag
          style = dict(padding = 10))
                



# Create app callback
@app.callback(Output(component_id='feature-graphic', component_property='figure'),
             [Input(component_id='xaxis', component_property='value'),
              Input(component_id='yaxis', component_property='value')])


# Update the graph
def update_graph(xaxis_name, yaxis_name):
    return {'data': [go.Scatter(x = df[xaxis_name],
                                y = df[yaxis_name],
                                text = df['name'],
                                mode = 'markers',
                                marker = {'size':12,
                                              'opacity':0.5,
                                              'line':{'width':0.5, 'color':'white'}})],
    
            'layout': go.Layout(title = 'Dashboard',
            xaxis = dict(title = xaxis_name.title()),
            yaxis = dict(title = yaxis_name.title()),
            #margin = dict(l = 40, b = 40, t = 10, r = 0),
            hovermode = 'colsest')}


# Run the app
if __name__ == '__main__':
    app.run_server()


