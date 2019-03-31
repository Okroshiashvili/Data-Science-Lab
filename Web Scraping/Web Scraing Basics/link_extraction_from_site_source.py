"""
Created on Sun Mar 31 2019

@author: Nodar Okroshiashvili
"""

from bs4 import BeautifulSoup
import requests

url = "http://example.com/"

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
tag_list = []
for tag in tags:
    tag_list.append(tag.get('href'))

# tag_list stores all the extracted links from website source
    
  