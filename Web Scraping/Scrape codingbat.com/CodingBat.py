


"""

We ar going to scrape codingbat.com

Particularly we have to scrape questions with examples in Java part

"""


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


user_agent = UserAgent()


main_url = 'http://codingbat.com/java'
base_url = 'http://codingbat.com'


page = requests.get(main_url,headers={'user-agent':user_agent.chrome})

soup = BeautifulSoup(page.content,'lxml')


# Finds all div tags with attribute class 'summ'
all_divs = soup.find_all('div',class_='summ')

# The for loop goes into each div tag extracts link tag and
# concatenate base url with extracted link tag(relative url) to go into topic page
for div in all_divs:
    print(base_url + div.a['href'])


# For loop in list comprehension to extract all links
all_links = [base_url + div.a['href'] for div in all_divs]
# These links are necessary to open each section ad extract question with example


for link in all_links:
    inner_page = requests.get(link,headers={'user-agent':user_agent.chrome})
    inner_soup = BeautifulSoup(inner_page.content,'lxml')
    div = inner_soup.find('div',class_='tabc')
    # tabc tag has child "table" which contains all the links for questions
    # the table tag have children "td" tags which contains links to each question
    # Below code gives link for each question in first topic
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]
    # Above for loop only goes first topic and extracts question links from it
    
    # Below for loop goes into each topic and gathers all question links
    for question_link in question_links:
        final_page = requests.get(question_link)
        final_soup = BeautifulSoup(final_page.content, 'lxml')
        indent_div = final_soup.find('div', attrs={'class':'indent'})
        
        # This gives problem statement
        problem_statement = indent_div.table.div.string
        

        # examples are siblings of last div tag
        # so, we have to go through each sibling tag and extract example text
        # code below return generator object
        # we need to loop this generator object
        siblings_of_statement = indent_div.table.div.next_siblings

        examples = [sibling for sibling in siblings_of_statement if sibling.string is not None]

        print(problem_statement)
        for example in examples:
            print(example)

        print('\n\n\n')



