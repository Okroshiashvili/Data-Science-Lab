"""
Created on Wed Mar 13 2019

@author: Nodar Okroshiashvili
"""




from bs4 import BeautifulSoup
import requests 



# Define the URL
url = "https://boston.craigslist.org/search/sof"


# Create the response object to get the webpage
response = requests.get(url)

# Print the reponse object
print(response)

# If output is "Response 200" means we connected to the web page successfuly



# Extract source code of the web page
data = response.text


# Create BeautifulSoup object from data to parse the html
soup = BeautifulSoup(data, 'html.parser')



# Find all "links" in soup object
# or tags "a"
tags = soup.find_all('a')



for tag in tags:
    print(tag.get('href'))



# Scrape job titles
titles = soup.find_all('a', {"class":"result-title"})


for title in titles:
    print(title.text)



# Extract job addresses
addresses = soup.find_all('span', {'class':'result-hood'})


for address in addresses:
    print(address.text)



"""
This is nearly perfect to start and know the mechanics of web scraping.
However, extraction of data seperatly can cause mismatch.
We need to extract all job details at once

"""


jobs = soup.find_all('p', {'class':'result-info'})



for job in jobs:
    title = job.find('a', {'class':'result-title'}).text
    location_tag = job.find('span', {'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date = job.find('time', {'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    
    # Extract job description
    
    # Go inside each link for a job and extract its description
    job_response = requests.get(link)
    job_data = job_response.text
    # Parse with BeautifulSoup
    job_soup = BeautifulSoup(job_data, 'html.parser')
    
    # Extract job description
    job_description = job_soup.find('section', {'id':'postingbody'}).text
    
    # Extract job attributes such as salary and so on
    job_attributes_tag = job_soup.find('p', {'class':'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else 'N/A'

    print('Job Title:', title, '\nLocation:', location, '\nDate:', date, '\nLink:', link,'\n', job_attributes, '\nJob Description:', job_description,'\n---')




"""

The tags, classes and identifiers Iused here are not unique for each website.
If you diced to scrape other website you should take a look at developer tool
and identify proper tags to scrape

"""


