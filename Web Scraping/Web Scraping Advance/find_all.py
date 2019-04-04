"""
Created on Wed Apr  3 2019

@author: Nodar Okroshiashvili
"""


from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)



# name parameter accepts regex object, string, boolean, and function

a_tags = soup.find_all('a')

print(a_tags)

# attrs parameter accepts dictionary

attr = {'class':'story'}
first_a = soup.find_all(attrs=attr)
print(first_a)


# limit parameter pose the limit of search result
# limit=2 means that "find_all" method only finds first two 'a' tags

a_tags = soup.find_all('a',limit=2)
print(a_tags)


