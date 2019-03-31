"""
Created on Sun Mar 31 2019

@author: Nodar Okroshiashvili
"""


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



# Function to read html file

def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data


# Read the file
html_file = read_file()


# For parsing html we can use lxml or html.parser
soup = BeautifulSoup(html_file,'html.parser')

# soup = BeautifulSoup(html_file,'lxml')

# soup prettify - prints html file with correct indentation

print(soup.prettify())



"""
Let see google.com html structure

"""


ua = UserAgent()

header = {'user-agent':ua.chrome}

# Get the response
google_page = requests.get('https://www.google.com',headers=header)

# Create BeautifulSoup object
soup = BeautifulSoup(google_page.content,'lxml')

# Print prettified html source file for google.com
print(soup.prettify())




