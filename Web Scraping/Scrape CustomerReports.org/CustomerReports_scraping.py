"""
Created on Sat Apr  6 2019

@author: Nodar Okroshiashvili
"""



from bs4 import BeautifulSoup



def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# Find all div tags with attribute class=entry-letter
all_divs = soup.find_all('div',attrs={'class':'entry-letter'})


# Finds first div tag, after that finds child f first div tag,
# after that finds a tag of div tag then span tag and extracts string from it
# In this case the names of products
products = [div.div.a.span.string for div in all_divs]

for product in products:
    print(product)




# Extract product name with its link and put inside dictionary


# product name - key 
# product link - value
products = {}


product_names = [div.div.a.span.string for div in soup.find_all('div',class_='entry-letter')]

product_links = [div.div.a['href'] for div in soup.find_all('div',class_='entry-letter')]

products = {div.div.a.span.string:div.div.a['href'] for div in soup.find_all('div',class_='entry-letter')}

for key,value in products.items():
    print(key , '   -->',value)







