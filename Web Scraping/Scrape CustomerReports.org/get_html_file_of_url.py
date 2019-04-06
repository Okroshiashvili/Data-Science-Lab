"""
Created on Sat Apr  6 2019

@author: Nodar Okroshiashvili
"""



import requests
from fake_useragent import UserAgent


# desired url
url = 'http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'

# output file name
file_name = 'consumer_reports.txt'

user_agent = UserAgent()

page = requests.get(url,headers={'user-agent':user_agent.chrome})
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)

