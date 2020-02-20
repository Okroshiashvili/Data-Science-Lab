


"""
This script will make regular API calls to http://data-live.flightradar24.com
to obtain updated total worldwide flights data.
This version continuously updates the number of flights worldwide,
and graphs those results over time.
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests


# Create the app
app = dash.Dash()



# Define app layout
app.layout = html.Div([
        html.Div([
                html.Iframe(src = 'https://www.flightradar24.com', height = 500,
                            width = 1200)
                ]),
                
        html.Div([
                html.Pre(
                        id = 'counter_text',
                        children = 'Active flights worldwide:'),
                 dcc.Graph(id='live-update-graph', style={'width':1200}),
                 dcc.Interval(
                         id='interval-component',
                         interval = 6000, # equal to 6 second
                         n_intervals = 0)])
        ])


# Set counter variable as a list
counter_list = []



@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])
# Function to scrape flights web-site and update layout
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # A fake header is necessary to access the site:
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return 'Active flights worldwide: {}'.format(counter)



@app.callback(Output('live-update-graph','figure'),
              [Input('interval-component', 'n_intervals')])

# Update graph
def update_graph(n):
    fig = go.Figure(
        data = [go.Scatter(
        x = list(range(len(counter_list))),
        y = counter_list,
        mode='lines+markers'
        )])
    return fig



# Run the app
if __name__ == '__main__':
    app.run_server()





"""

After running the script the website does not show up.
I tried to find the way out but with no success.
Then I figureout that the administration of the site has changed the site
to block it showing in Iframe tag

"""



