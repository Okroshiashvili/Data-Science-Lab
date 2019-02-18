# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 2019

@author: Nodar Okroshiashvili
"""


import dash
import dash_core_components as dcc
import dash_html_components as html


# Create the application
app = dash.Dash()


# Define styling colors
colors = {'background':'#111111', 'text':'#7FDBFF'}


# Style H1 html component





# App layout
app.layout = html.Div(children = [html.H1(
                                        children = 'Hello Dash!',
                                        style = {
                                                'textAlign':'center',
                                                'color':colors['text']}),
                                  dcc.Graph(id = 'example',
                                            figure = {'data':[{'x':[1,2,3],
                                                               'y':[4,1,2],
                                                               'type':'bar',
                                                               'name':'SF'},
                                                                {'x':[1,2,3],
                                                                 'y':[2,4,5],
                                                                 'type':'bar',
                                                                 'name':'Montreal'},
                                                                 ],
                                                      'layout':{
                                                              'plot_bgcolor':colors['background'],
                                                              'paper_bgcolor':colors['background'],
                                                              'font':{'color':colors['text']},
                                                              'title':'Dash Data Visualization'
                                                              }})
], style={'background':colors['background']}
)


# Run the server
if __name__ == '__main__':
    app.run_server()



