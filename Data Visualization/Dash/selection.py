


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

                              })],style = {'width':'30%', 'display':'inline-block'}),

        html.Div([html.Pre(id='selection', style={'paddingTop':25})],
             style = {'width':'30%', 'display':'inline-block','verticalAlign':'top'})
        ])






@app.callback(Output('selection', 'children'),
             [Input('wheels-plot', 'selectedData')])
# Function to update graph
def callback_image(selectedData):
    return json.dumps(selectedData, indent = 2)



# Run the application
if __name__ == '__main__':
    app.run_server()


