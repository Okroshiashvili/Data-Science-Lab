


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


# Read the data
df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'cb5392c35661370d95f300086accea51/raw/'
        '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
        'indicators.csv')




# Create the app
app = dash.Dash()


# Available indicator in df
available_indicators = df['Indicator Name'].unique()


# Create the app layout
app.layout = html.Div([
        html.Div([
                html.Div([
                        dcc.Dropdown(
                                id = 'xaxis-column',
                                options = [{'label':i, 'value':i} for i in available_indicators],
                                # Set initial value for dropdown
                                value = 'Fertility rate, total (births per woman)'
                                ),
                        dcc.RadioItems(
                                id = 'xaxis-type',
                                options = [{'label':i, 'value':i} for i in ['Liner', 'Log']],
                                value = 'Linear',
                                labelStyle={'display':'inline-block'}
                                )
                        ], # Style for innermost Div
                         style = {'width':'40%', 'display':'inline-block'}),
                 html.Div([
                         dcc.Dropdown(
                                 id = 'yaxis-column',
                                 options=[{'label':i, 'value':i} for i in available_indicators],
                                 value = 'Life expectancy at birth, total (years)'),
                                 
                         dcc.RadioItems(
                                 id = 'yaxis-type',
                                 options=[{'label':i, 'value':i} for i in ['Linear', 'Log']],
                                 value = 'Linear',
                                 labelStyle = {'diplay':'inline-block'}
                                 )
                            ], 
                            style = {'width':'40%','float':'right', 'display':'inline-block'})
                         
                         ]),
                dcc.Graph(id = 'indicator-graphic'),
                
                dcc.Slider(
                        id = 'year--slider',
                        min = df['Year'].min(),
                        max = df['Year'].max(),
                        value = df['Year'].max(),
                        step = None,
                        marks = {str(year):str(year) for year in df['Year'].unique()})
                  
                ],style = {'padding':10})




# Create app callback
@app.callback(
        Output(component_id='indicator-graphic', component_property='figure'),
        [Input(component_id='xaxis-column', component_property='value'),
         Input(component_id='yaxis-column', component_property='value'),
         Input(component_id = 'xaxis-type', component_property='value'),
         Input(component_id='yaxis-type', component_property = 'value'),
         Input(component_id = 'year--slider', component_property='value')])

# Function which update the gaph object
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]
    
    return {'data':[go.Scatter(
            x = dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y = dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text = dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode = 'markers',
            marker = {
                    'size':15,
                    'opacity':0.5,
                    'line':{'width':0.5, 'color':'white'}
                    }
            )],
           'layout':go.Layout(
                   xaxis = {'title':xaxis_type,
                            'type':'linear' if xaxis_column_name == 'Linear' else 'log'
                           },
                    yaxis = {'title':yaxis_column_name,
                             'type':'linear' if yaxis_column_name == 'Linear' else 'log'
                            },
                    margin = {'l':40, 'b':40, 't':10, 'r':0},
                    hovermode = 'closest'
                   )
           }



# Run the application
if __name__ == '__main__':
    app.run_server()
               


