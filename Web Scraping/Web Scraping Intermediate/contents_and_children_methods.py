"""
Created on Sun Mar 31 2019

@author: Nodar Okroshiashvili
"""


from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')



# tag.contents method returns a list of children
body = soup.body


for child in body.contents:
    print(child if child is not None else '',end='\n\n\n\n')

"""

body.content method gives all the information what is included inside
body rag

"""




# .children method returns an iterator
for child in body.children:
    print(child if child is not None else '', end='\n\n\n\n')



"""

body.children method gives all the information what is included inside
the children tags of body tag

"""




