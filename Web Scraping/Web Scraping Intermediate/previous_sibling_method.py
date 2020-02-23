


from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body

# contents - html

print(soup.html.contents)

# .previous_sibling method gives all the previous sibling tags of a given tag

print(body.previous_sibling.previous_sibling)
