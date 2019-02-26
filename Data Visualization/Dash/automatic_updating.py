# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 2019

@author: Nodar Okroshiashvili
"""




"""

This script automatically refreshes the page and counts that refreshes.

I set manually the time interval at which the refresh will happen

"""



import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output



# Create the app
app = dash.Dash()



# Create the layout
app.layout = html.Div([
        html.H1(id = 'live-update-text'),
        dcc.Interval(id = 'interval-component',
                     interval = 2000, # 2000 millisecont equal to 2 second
                     n_intervals = 0)])



@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])

# Function updates the layout every 2 second
def update_leyout(n):
    return 'Crash free for {} refreshes'.format(n)



# Run the app
if __name__ == '__main__':
    app.run_server()


