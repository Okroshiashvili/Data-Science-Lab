# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 2019

@author: Nodar Okroshiashvili
"""



#   Dash callbacks with graphs



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import pandas as pd



# Read the data
df = pd.read_csv('data/gapminderDataFiveYear.csv')


# Create app
app = dash.Dash()




# Create option list of dictionaries
year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})



# Create app layout
app.layout = html.Div([
        dcc.Graph(id = 'graph'),
        dcc.Dropdown(id = 'year-picker',
                     options = year_options,
                     # Default value for dropdown
                     value = df['year'].min())
        ])



# Add calback
@app.callback(Output(component_id = 'graph', component_property='figure'),
              [Input(component_id = 'year-picker', component_property='value')])

# Function to update the graph
def update_figure(selected_year):
    
    # Data only for selected year from dropdown
    filtered_df = df[df['year'] == selected_year]
    
    # Create traces for each continent
    traces = []
    
    for continent in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent]
        
        # Create Plotly scatter for continent
        traces.append(go.Scatter(
                x = df_by_continent['gdpPercap'],
                y = df_by_continent['lifeExp'],
                text = df_by_continent['country'],
                mode = 'markers',
                opacity = 0.7,
                marker = {'size':12},
                name = continent
            ))
    return {'data': traces,
            'layout':go.Layout(title = 'Life Expectancy vs GDP Per Capita',
            xaxis = dict(title = 'GDP Per Capita', type = 'log'),
            yaxis = dict(title = 'Life Expectancy'),
            hovermode = 'closest'
        )}



# Run the application
if __name__ == '__main__':
    app.run_server()


