


"""
To the right of the scatter there is line, which represents acceleration
of a selected vehicle.

The steeper the line, the quicker acceleration.



Data has acceleration column that represents acceleration in seconds. We need
to represent this as a slope. For this I use the followinf formula


acceleration = [(60 miles per hour)/(60 minutes per hour)]/(? seconds)/(60 seconds/minute)

The greater the number of seconds the slower the acceleration and 
the flatter the slope

"""



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random



# Read the data
df = pd.read_csv('../data/mpg.csv')


# Create the app
app = dash.Dash()



# Add random "jitter" to model_year to spread out the plot
df['year'] = df['model_year'] + random.randint(-4,5,len(df))*0.10


# Create app layout
app.layout = html.Div([
        html.Div([ # this Div contains our scatter plot
                dcc.Graph(
                        id = 'mpg_scatter',
                        figure = {
                                'data':[go.Scatter(
                                        x = df['year'] + 1900,
                                        y = df['mpg'],
                                        text = df['name'],
                                        hoverinfo = 'text',
                                        mode = 'markers')],
                                 'layout': go.Layout(
                                         title = 'MPG Dataset',
                                         xaxis = {'title':'Model Year'},
                                         yaxis = {'title':'Miles Per Galon'},
                                         hovermode = 'closest')
                                 }
                           )],style={'width':'50%', 'display':'inline-block'}),
      html.Div([# this Div contains our output graph and vehicle stats
              dcc.Graph(
                      id = 'mpg_line',
                      figure = {
                              'data':[go.Scatter(
                                      x = [0,1],
                                      y = [0,1],
                                      mode = 'lines')],
                                'layout': go.Layout(
                                        title='acceleration',
                                        margin = {'l':0})
                                }
                            ),
                dcc.Markdown(
                        id = 'mpg_stats')
                ], style ={'width':'20%', 'height':'50%', 'display':'inline-block'})
   ])





@app.callback(Output('mpg_line', 'figure'),
              [Input('mpg_scatter', 'hoverData')])
# Function to update the graph
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {'data':[go.Scatter(
            x = [0,1],
            y = [0, 60/df.iloc[v_index]['acceleration']],
            mode='lines',
            line = {'width':2 * df.iloc[v_index]['cylinders']}
            
            )],
           
           'layout':go.Layout(
            title=df.iloc[v_index]['name'],
            xaxis= {'visible':False},
            yaxis={'visible':False, 'range':[0,60/df['acceleration'].min()]},
            margin={'l':0},
            height=300)}
           
    return fig




@app.callback(Output('mpg_stats', 'children'),
              [Input('mpg_scatter', 'hoverData')])
# Returns back the stats of each car
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
    {} cylinders
    {}cc displacement
    0 to 60mph in {} seconds
    """.format(df.iloc[v_index]['cylinders'],
               df.iloc[v_index]['displacement'],
               df.iloc[v_index]['acceleration'])
    return stats
    

# Run the application
if __name__ == '__main__':
    app.run_server()



