


from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body

p = soup.body.p


# body - contents
# Prints children of body tag
print(body.contents)



# .next_sibling gives all the sibling tags on successive iteration

# Goes along each sibling tags and prints them

print(p.next_sibling.next_sibling)



