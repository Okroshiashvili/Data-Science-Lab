"""
Created on Sat Apr  6 2019

@author: Nodar Okroshiashvili
"""



from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.get('https://www.google.com')

# search tag using id
# this finds google's search bar

# search_bar = driver.find_element_by_id('gLFyf gsfi')
# do not use above command as google changed its id
search_bar = driver.find_element_by_xpath('//*[@name="q"]')

# this writes pre-defined text or search keywords in google search bar
search_bar.send_keys('I want to learn web scraping')


# submit the form
search_bar.submit()


# This is to wait 10 seconds and after that close driver object
sleep(10)


# We have to close driver object
driver.close()




