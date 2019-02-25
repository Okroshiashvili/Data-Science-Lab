# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 2019

@author: Nodar Okroshiashvili
"""



"""

Using Pandas DataReader, extracts the close price of stocks 
and visualize them.

"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd



# Read the data
nsdq = pd.read_csv('data/NASDAQcompanylist.csv')
# In this dataframe there are stock names for dropdown menu


# Set dataframe index
nsdq.set_index('Symbol', inplace = True)


# Make list of stock names
options = []

for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic, nsdq.loc[tic]['Name']), 'value': tic})



# Create the app
app = dash.Dash()


# Create the app layout
app.layout = html.Div([
        html.H1('Stock Ticker Dashboard'),
        html.Div([
           html.H3('Enter a stock symbol:', style={'padding':'30px'}),
           dcc.Dropdown(
                id='my_ticker_symbol',
                # Set default value
                value = ['TSLA'],
                multi = True)],
            style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
                
        html.Div([
                html.H3('Select start and end dates:'),
                dcc.DatePickerRange(
                        id='my_date_picker',
                        min_date_allowed = datetime(2015,1,1),
                        max_date_allowed = datetime.today(),
                        start_date = datetime(2018,1,1),
                        end_date = datetime.today())],
                style = {'display':'inline-block'}),
        
        html.Div([
                html.Button(
                        id='submit-button',
                        n_clicks = 0,
                        children = 'Submit',
                        style = {'fontSize':24, 'marginLeft':'30px'})],
                style = {'display':'inline-block'}),

        dcc.Graph(
                id = 'my_graph',
                figure = {'data':[{'x':[1,2], 'y':[3,1]}]}
                  )
        ])


# Create callback
@app.callback(Output('my_graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
               [State('my_ticker_symbol', 'value'),
               State('my_date_picker', 'start_date'),
               State('my_date_picker', 'end_date')])

# Function to upgrade graph
def upgrade_graph(n_clicks, stock_ticker, start_date, end_date):
    # Start date
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    # End date
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    # Traces containing stock(s) data from start to end
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, 'iex', start, end)
        traces.append({'x':df.index, 'y':df.close, 'name':tic})
    fig = {
            'data':traces,
            'layout':{'title':', '.join(stock_ticker) + 'Closing Prices'}
            }
    return fig




# Run the app
if __name__ == '__main__':
    app.run_server()




