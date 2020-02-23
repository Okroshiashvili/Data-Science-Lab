


import requests


'''
Most commonly two types of requests are used :

- GET           --> used to retrieve information
- POST          --> used to send information

'''


# requests.get(url)         -- response object

response = requests.get('https://www.google.com')



#content

# response.content



#Status codes
'''
1xx     Informational   100-199
2xx     Success         200-299
3xx     Redirection     300-399
4xx     Client Error    400-499
5xx     Server Error    500-599
'''

print(response.status_code)


#Headers returned

# response.headers

print(response.headers)


for key,value in response.headers.items():
    print(key,'   ',value)

