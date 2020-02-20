


"""
Scrape coinmarketcap.com
"""


import requests
from bs4 import BeautifulSoup


r=requests.get("https://coinmarketcap.com/currencies/bitcoin/",
                   headers={'User-Agent':'Mozilla/5.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")

value_raw=soup.find_all("span")



value_net=float(value_raw[1296].text)


