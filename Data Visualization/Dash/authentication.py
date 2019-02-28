# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 2019

@author: Nodar Okroshiashvili
"""




""""
When run, this app will require the authorization.
User name and password are hardcoded

"""


import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



# Username password pair for authentication
USERNAME_PASSWORD_PAIRS = [
        ['JamesBond', '123456'],['LouisArmstrong', 'satchmo']]



# Create the app
app = dash.Dash()


# Create authentication
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)



# App layout
app.layout = html.Div([
        dcc.RangeSlider(
                id = 'range-slider',
                min = -5,
                max = 6,
                marks = {i:str(i) for i in range(-5,7)},
                value = [-3, 4]),
                
        html.H1(id = 'product')
        ], style = {'width':'50%'})


@app.callback(Output('product', 'children'),
              [Input('range-slider','value')])

def update_value(value_list):
    return value_list[0] * value_list[1]


# Run the app
if __name__ == '__main__':
    app.run_server()

