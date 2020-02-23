


from bs4 import BeautifulSoup


def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# Accessing meta tag
# This gives only first occurrence of meta tag
meta = soup.meta


# tag methods

'''

name
-- attributes
.get() method
dictionary

'''
# To extract tag attribute
# ger method is used to get the value of any attribute
print(meta.get('charset'))

# Second way to get the value of attribute is to use dictionary
print(meta['charset'])


# modify attributes
body = soup.body

# give whole body tag
print(body)

# Modifies body tag attribute value
body['style'] = 'some style'


'''
 Multi valued attributes

'''

# Returns multivalued attributes
print(body['class'])




