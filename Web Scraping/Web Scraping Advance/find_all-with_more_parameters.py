


from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)



# string parameter searchs for navigable string in html tree

regex = re.compile('story')

tag = soup.find_all(string=regex)



# **kwargs or keyword arguments

tags = soup.find_all(class_='sister', id='link1')
for tag in tags:
    print(tag)

# to write the class attribute of a tag we have to use class_
# class with underscore, because simple class is a reserved keyword in Python



# recursive parameter
    
# If True (default state of parameter) recursively parse the whole tree
# If False it parse only direct children of given tag

title = soup.find_all('title',recursive=False)

print(title)



