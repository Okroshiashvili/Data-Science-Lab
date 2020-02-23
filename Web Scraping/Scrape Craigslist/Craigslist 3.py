


"""

             Save output in CSV file
             
             
This is the essentially the same code as Craigslist 2.py but instead of printing
the output this file saves the output in pandas DataFrame and exports it into
CSV file.

"""


from bs4 import BeautifulSoup
import requests 
import pandas as pd



url = "https://boston.craigslist.org/search/npo"



# Extract Job data

# Dict for scraped data
npo_jobs = {}

# Count the number of job postings
job_no = 0

while True:
    
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    jobs = soup.find_all('p', {'class':'result-info'})
    
    for job in jobs:
        
        # General Description
        title = job.find('a',{'class':'result-title'}).text
        location_tag = job.find('span',{'class':'result-hood'})
        location = location_tag.text[2:-1] if location_tag else 'N/A'
        date = job.find('time', {'class':'result-date'}).text
        link = job.find('a',{'class':'result-title'}).get('href')
        
        # Job Specific Description
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')
        job_description = job_soup.find('section',{'id':'postingbody'}).text
        job_attributes_tag = job_soup.find('p', {'class':'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else 'N/A'
        
        job_no += 1
        npo_jobs[job_no] = [title, location, date, link, job_attributes, job_description]
        
        
    url_tag = soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + url_tag.get('href')
    else:
        break
    
print("Total Jobs:", job_no)


# Append initial dict and convert into panda DataFrame
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index',
                                     columns = ['Job Title','Location','Date', 'Link', 'Job Attributes', 'Job Description'])



# Print first five rows
npo_jobs_df.head()

# Save as csv file
npo_jobs_df.to_csv('npo_jobs.csv')



