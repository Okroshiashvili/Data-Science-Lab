


"""
Reflects how many time we refresh the page.
In other words app layout updates automatically while refreshing the page

"""




import dash
import dash_html_components as html


# Create app
app = dash.Dash()


crash_free = 0 # Refresh counter

# Function to update layout
def refresh_layout():
    global crash_free # Put counter inside function
    # We defined counter outide the function, that's why we need
    # global keyword. By using global, out function has access to counter
    crash_free += 1 # update rule for counter
    return html.H1('Crash free for {} refreshes'.format(crash_free))
    



# Define app layout
    
# Now we see that app layout will change every time we refresh the app
app.layout = refresh_layout 



# Run the application
if __name__ == '__main__':
    app.run_server()

