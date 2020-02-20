


"""

dash.dependencies.State gives us possibility to delay the input.

It's convenient for "submit" button

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State



# Create the app
app = dash.Dash()


# Create app layout
app.layout = html.Div([
        dcc.Input(id='number-in',
                  value = 1,
                  style = {'fontSize':24}),
        html.Button(id='submit-button',
                    n_clicks = 0,
                    children = 'Submit Here',
                    style = {'fontSize':24}),        
        html.H1(id = 'number-out')
        ])





@app.callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('number-in', 'value')])

def output(n_clicks, number):
    return "{} displayed after {} clicks".format(number, n_clicks)





if __name__ == '__main__':
    app.run_server()



