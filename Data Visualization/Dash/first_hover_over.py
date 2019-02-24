# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 2019

@author: Nodar Okroshiashvili
"""



"""

Hovering over the data point on the graph affect another part of figure


"""



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json



# Read the data
df = pd.read_csv('data/wheels.csv')


# Create the app
app = dash.Dash()


# Create the leyout
app.layout = html.Div([
        html.Div([dcc.Graph(id='wheels-plot',
                           figure = {'data':[go.Scatter(
                                   x = df['color'],
                                   y = df['wheels'],
                                   dy = 1,
                                   mode = 'markers',
                                   marker = {'size':12,
                                             'color':'rbg(51,204,153)',
                                             'line':{'width':2}}
                                   )],

                                     'layout':go.Layout(
                                             title='Wheels & Colors Scatterplot',
                                             xaxis = {'title':'Colors'},
                                             yaxis = {'title':'# of wheels', 'nticks':3},
                                            hovermode = 'closest')

                              })],style = {'width':'30%', 'float':'left'}),

        html.Div([html.Pre(id='hover-data', style={'paddingTop':35})],
             style = {'width':'30%'})
        ])






@app.callback(Output('hover-data', 'children'),
             [Input('wheels-plot', 'hoverData')])
# Function to update graph
def callback_image(hoverData):
    return json.dumps(hoverData, indent = 2)



# Run the application
if __name__ == '__main__':
    app.run_server()


