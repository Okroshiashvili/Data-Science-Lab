"""
Created on Sun Feb 10 2019

@author: Nodar Okroshiashvili
"""

"""
Scrape bitcoin charts website and plots teal time price movement for

bitstamp USD and EUR


"""


# https://bitcoincharts.com/markets/



from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.layouts import layout
from bokeh.plotting import figure
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from math import radians
from pytz import timezone

# Create figure
f=figure(x_axis_type='datetime')

# Create webscraping function
def extract_value(currancy_name="bitstampUSD"):
    r=requests.get("https://bitcoincharts.com/markets/"+currancy_name+".html",
                   headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup=BeautifulSoup(c,"html.parser")
    value_raw=soup.find_all("span")
    value_net=float(value_raw[1].text)
    return value_net

# Create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

# Create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)

# Create periodic function
def update():
    new_data=dict(x=[datetime.now(tz=timezone('Asia/Tbilisi'))],
                     y=[extract_value(select.value)])
    source.stream(new_data,rollover=200)
    print(source.data)

def update_intermediate(attr, old, new):
    source.data=dict(x=[],y=[])
    update()
    
f.xaxis.formatter=DatetimeTickFormatter(
seconds=["%Y-%m-%d-%H-%m-%S"],
minsec=["%Y-%m-%d-%H-%m-%S"],
minutes=["%Y-%m-%d-%H-%m-%S"],
hourmin=["%Y-%m-%d-%H-%m-%S"],
hours=["%Y-%m-%d-%H-%m-%S"],
days=["%Y-%m-%d-%H-%m-%S"],
months=["%Y-%m-%d-%H-%m-%S"],
years=["%Y-%m-%d-%H-%m-%S"],
)

f.xaxis.major_label_orientation=radians(90)

# Create Select widget
options=[("bitstampUSD","Bitstam USD"),("bitstampEUR","Bitstamp EUR")]

select=Select(title="Currancy Name",value="bitstampUSD",options=options)
select.on_change("value",update_intermediate)

# Add figure to curdoc
lay_out=layout([[f],[select]])
curdoc().add_root(lay_out)

# Configure callback
curdoc().add_periodic_callback(update,2000)


