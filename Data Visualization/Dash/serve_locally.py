


"""
To serve dash app locally and not ot send any sensitive information
online for processing, put this code before running server

"""

# Run locally
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


# Run the application
if __name__ == '__main__':
    app.run_server()


