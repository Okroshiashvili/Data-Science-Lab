"""
Created on Sat Feb  9 2019

@author: Nodar Okroshiashvili
"""



from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup

# Create figure
f=figure(x_range=(0,11),y_range=(0,11))

# Create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

# Create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)


# Create webscraping function
def extract_value():
    r=requests.get("https://coinmarketcap.com/currencies/bitcoin/",
                   headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup=BeautifulSoup(c,"html.parser")
    value_raw=soup.find_all("span")
    value_net=float(value_raw[1296].text)
    return value_net

# Create periodic function
def update():
    new_data=dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)
    print(source.data)

# Add figure to curdoc
curdoc().add_root(f)
# Configure the callback
curdoc().add_periodic_callback(update,1000)



