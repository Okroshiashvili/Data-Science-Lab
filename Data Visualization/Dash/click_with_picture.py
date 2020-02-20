


"""

Inseat of hover over data, now we have to click the data point

"""



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64




# Read the data
df = pd.read_csv('data/wheels.csv')


# Create the app
app = dash.Dash()



# Read the image files
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())




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

        html.Div([
                html.Img(id='click-image', src = 'children', height = 300)
                ],style = {'paddingTop':35})
        ])






@app.callback(Output('click-image', 'src'),
             [Input('wheels-plot', 'clickData')])
# Function to update graph
def callback_image(clickData):
    wheel = clickData['points'][0]['y']
    color = clickData['points'][0]['x']
    path = '../data/Images/'
    return encode_image(path + df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])



# Run the application
if __name__ == '__main__':
    app.run_server()



