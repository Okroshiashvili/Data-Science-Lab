


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
fig = tools.make_subplots(rows = 2, cols = 1, specs = [[{}], [{'colspan':1}]],
                          subplot_titles = ('First Plot', 'Second Plot'))



# Append figure with traces
fig.append_trace(trace_1,1,1)
fig.append_trace(trace_2,2,1)



# Update the layout
fig['layout'].update(title = 'Scatter Plots', showlegend=True)


# # Create layout
# layout = go.Layout(title = 'My Scatter Plots',
#                   xaxis = dict(title = 'X axis'),
#                   xaxis2 = dict(title = 'X axis 2'),
#                   yaxis = dict(title = 'Y axis'),
#                   yaxis2 = dict(anchor = 'x2'))



# # Figure object
# fig = go.Figure(data = data, layout = layout)




# Add figure object to dash app
app.layout = html.Div(children = [
        dcc.Graph(id = 'scatter', figure = fig)])



# Run the application
if __name__ == '__main__':
    app.run_server()

