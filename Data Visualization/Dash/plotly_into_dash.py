


"""
Import and insert Plotly plot into Dash dashboard
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np



# Create application object
app = dash.Dash()


# Create data
np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)



# Create plotly graph inside dash

app.layout = html.Div(children = [dcc.Graph(id = 'scatterplot1',
                    figure = {'data':[
                            go.Scatter(
                                    x = random_x,
                                    y = random_y,
                                    mode = 'markers',
                                    marker = dict(size = 12,
                                                  color = 'rgb(27,04,92)',
                                                  symbol = 'square',
                                                  line = dict(width = 2))
                                    )], # Plotly's data list goes into
                                        # dash's components as a value of 
                                        # figure dictionary and key is 'data'
                              'layout':go.Layout(title = 'My Scatter Plot',
                                                 xaxis = dict(title = 'X Axis'),
                                                 yaxis = dict(title = 'Y Axis'))}
                                 ),
                              # This is second plot
                              dcc.Graph(id = 'scatterplot2',
                    figure = {'data':[
                            go.Scatter(
                                    x = random_x,
                                    y = random_y,
                                    mode = 'markers',
                                    marker = dict(size = 12,
                                                  color = 'rgb(27,16,193)',
                                                  symbol = 'circle',
                                                  line = dict(width = 2))
                                    )], # Plotly's data list goes into
                                        # dash's components as a value of 
                                        # figure dictionary and key is 'data'
                              'layout':go.Layout(title = 'Second Plot',
                                                 xaxis = dict(title = 'X Axis'),
                                                 yaxis = dict(title = 'Y Axis'))}
                                 )])





# Run the application
if __name__ == '__main__':
    app.run_server()

