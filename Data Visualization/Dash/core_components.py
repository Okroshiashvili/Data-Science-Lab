


import dash
import dash_html_components as html
import dash_core_components as dcc


# Dash application
app = dash.Dash()


# Add layout
app.layout = html.Div([
        # Add label
        html.Label('Dropdown'),
        # Add list of dictionaries as options
        dcc.Dropdown(options = 
                     [{'label': 'New York City',
                                 'value':'NYC'},
                                {'label':'San Francisco',
                                 'value':'SF'},
                                 {'label':'Montreal',
                                  'value':'MTL'}],
                    value = 'MTL'),
        
        # Multi Select Dropdown
        html.Label('Multi-Select-Dropdown'),
        dcc.Dropdown(
                options = [
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
        value = ['MTL', 'SF'],
        multi = True),
        
        # Slider
        html.Label('Slider'),
        html.P(
                dcc.Slider(
                        min = -5,
                        max = 10,
                        step = 0.5,
                        marks = {i: i for i in range(-5,11)},
                        value = -3)),
                
        # Radio Button
        html.Label('Radio Items'),
        dcc.RadioItems(
                options = [
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                        ],
                value = 'MTL')],
        style = {'width':'50%'})


# Run the application
if __name__ == '__main__':
    app.run_server()


