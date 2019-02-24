# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 2019

@author: Nodar Okroshiashvili
"""



"""

Determine the density of selected points in a region

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np



# Create the application
app = dash.Dash()


#Create the artificial data
np.random.seed(10)
x1 = np.linspace(0.1, 5, 50) # Left half
x2 = np.linspace(5, 0.1, 50) # Right half
y = np.random.randint(0,50,50) # 50 random points


# Create three "half DataFrames
df1 = pd.DataFrame({'x':x1, 'y':y})
df2 = pd.DataFrame({'x':x1, 'y':y})
df3 = pd.DataFrame({'x':x2, 'y':y})



# Combine them in one DataFrame
# df1 and df2 points overlap
df = pd.concat([df1, df2, df3])



# Create app layout
app.layout = html.Div([
        html.Div([
        dcc.Graph(id='plot',
                    figure ={'data':[go.Scatter(
                            x = df['x'],
                            y = df['y'],
                            mode='markers')],
                            'layout':go.Layout(title = 'Random Scatterplot',
                                               hovermode='closest')}
        )], style ={'width':'30%', 'display':'inline-block'}),
                            
        html.Div([
                html.H1(id='density', style={'paddingTop':25})
                ], style = {'width':'30%', 'display':'inline-block','verticalAlign':'top'})
  ])



@app.callback(Output('density', 'children'),
              [Input('plot', 'selectedData')])
# Define function to calculate density
def find_density(selectedData):
    # Calculate the density
    pts = len(selectedData['points']) # How many points are there
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x-min_x)*(max_y-min_y) # calculate the selected area
    d = pts/area # Density is the number of points in selected area
    return 'Density = {:.2f}'.format(d)    




# Run the application
if __name__ == '__main__':
    app.run_server()




