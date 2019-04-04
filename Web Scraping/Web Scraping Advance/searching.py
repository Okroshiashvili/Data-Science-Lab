"""
Created on Wed Apr  3 2019

@author: Nodar Okroshiashvili
"""




from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# most popular methods for searching are:
# Those two methods takes the tag name as a parameter

# find()
# find_all()        


# Finds all 'a' tag
print(soup.find_all('a'))

# regular expression

# We can find tag names with regular expressions
# For exmaple find tag names which start with b

regex = re.compile('^b')

for tag in soup.find_all(regex):
    print(tag.name)



# Find tag names which contains t

regex = re.compile('t')

for tag in soup.find_all(regex):
    print(tag.name)




# We can put a list into search pattern
# Below patter finds all 'a' and 'b' tags

for tag in soup.find_all(['a','b']):
    print(tag.name)



# We can also put a function into find_all method

def has_class(tag):
    return tag.has_attr('class')

# This function searchs if given tag has attribute "class"
# If has function returns True, otherwise False
    

for tag in soup.find_all(has_class):
    print(tag.name)







