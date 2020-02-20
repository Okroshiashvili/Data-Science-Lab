


"""
More convenient way to insert multiple Plotly plots into Dash
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly import tools
import numpy as np


# Create application object
app = dash.Dash()


# Create data
np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)



# Create the traces
trace_1 = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers',
        marker = dict(
                size = 12,
                color = 'rgb(27,04,92)',
                symbol = 'circle',
                line = dict(width = 2)))
        
        
        
trace_2 = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers',
        marker = dict(
                size = 12,
                color = 'rgb(16,08,91)',
                symbol = 'square',
                line = dict(width = 2)))



# Figure object
fig = tools.make_subplots(rows = 2, cols = 1)



# Append figure with traces
fig.append_trace(trace_1,1,1)
fig.append_trace(trace_2,2,1)



# Update the layout
fig['layout'].update(title = 'Scatter Plots')


# # Create layout
# layout = go.Layout(title = 'My Scatter Plot',
#                   xaxis = dict(title = 'X axis'),
#                   yaxis = dict(title = 'Y axis'))



# # Figure object
# fig = go.Figure(data = data, layout = layout)




# Add figure object to dash app
app.layout = html.Div(children = [
        dcc.Graph(id = 'First Scatter', figure = fig),
        dcc.Graph(id = 'Second Scatter', figure = fig)])



# Run the application
if __name__ == '__main__':
    app.run_server()



