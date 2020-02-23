


from bs4 import BeautifulSoup



def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# Navigable strings


# string inside a tag   - .string

title = soup.title

# Print the title of the tag
print(title)

# Gives whole tag
# Each tag has method '.string'
print(title.string)



# .replace_with("") function

print(title)

# Replaces the contents of the string
title.string.replace_with("title has been changed")


print(title)




