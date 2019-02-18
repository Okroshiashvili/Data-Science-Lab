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
from datetime import datetime
from math import radians
from pytz import timezone

#create figure
f=figure(x_axis_type='datetime')

#create webscraping function
def extract_value():
    r=requests.get("https://coinmarketcap.com/currencies/bitcoin/",
                   headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup=BeautifulSoup(c,"html.parser")
    value_raw=soup.find_all("span")
    value_net=float(value_raw[1296].text)
    return value_net

#create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

#create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)

#create periodic function
def update():
    new_data=dict(x=[datetime.now(tz=timezone('Asia/Tbilisi'))],y=[extract_value()])
    source.stream(new_data,rollover=200)
    print(source.data)
    
    
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

#add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update,2000)

