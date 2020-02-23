


from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

title = soup.title

# Parent tag of title tag
parent = title.parent


# .parent

p = soup.p
# Prints the name of the parent tag of p tag
# .name method gives us tag's name
print(p.parent.name)



# html

# who is the parent of the source html file?
html = soup.html

print(type(html.parent))
#bs4 is the parent of html document


# who is the parent of BeautifulSoup
print(soup.parent)

# Returns None as there is no parent for BeautifulSoup

"""
Hierarchy is the following:
    BeautifulSoup if the parent of each tag we have in html document
    then html tag is parent of head and body tag
    then head tag is parent of title tag
    then body tag is the parent of b and p tags
    
"""





# .parents method returns a list ( generator )  of all parents of a given tag

link = soup.a

for parent in link.parents:
    print(parent.name)

