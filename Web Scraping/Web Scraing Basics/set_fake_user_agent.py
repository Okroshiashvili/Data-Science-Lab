


import requests
from fake_useragent import UserAgent

# Background on user-agents

ua = UserAgent()

header = {'user-agent':ua.chrome}

"""
If we do not add 'header' this means that robot or program sends requests
to the server. Websites can catch this behavior and block it.
That's why wee need fake user agent module to pass this shield.
In other words, we want website to see that real user sends request not program

"""

page = requests.get('https://www.google.com',headers=header)
print(page.content)

# Background on Timeout

"""
timeout means that after 3 seconds if server does not response code moves
along, or it does not wait indefinitely to the server

"""

page = requests.get('https://www.google.com',timeout=3)


