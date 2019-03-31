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


# .contents method returns us DIRECT children of the given tag
body = soup.body

children = [child for child in body.contents if child != '\n']
print(children)

print(len(children))
# In this case navigable string is a child of title tag and is not 
# direct child of head tag




# Each tag has descendants method
# children and descendants  method are pritty much the same methods

# .descendants method returns us ALL the children of the given tag
for index,child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '\\n')




