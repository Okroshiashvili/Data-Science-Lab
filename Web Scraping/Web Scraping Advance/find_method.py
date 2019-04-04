"""
Created on Thu Apr  4 2019

@author: Nodar Okroshiashvili
"""


from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Signature: find(name, attrs, recursive, string, **kwargs)

# Does not have limit argument as it returns single object

# returns a single object if found
# in case of multiple objects, it returns the first one it finds

tag = soup.find('a')
print(tag)


