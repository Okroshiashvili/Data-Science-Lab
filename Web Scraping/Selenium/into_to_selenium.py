"""
Created on Sat Apr  6 2019

@author: Nodar Okroshiashvili
"""


from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup




"""

With selenium we need web driver for our browser.
If you use google chrome, you can download chrome driver from here:
    
http://chromedriver.chromium.org/downloads


In linux (my OS) I extracted downloaded zip file and placed
exe file in "/home/nodo/bin"


I did this in order not to write chrome driver path everytime


"""

# IF you did not locate exe file in user/bin or user/local/bin
# then you have to specify the driver path while creating driver object
# driver object is browser which you can programatically control
driver = webdriver.Chrome('/Users/waqarjoyia/Downloads/chromedriver')



# open some page using get method
driver.get('https://www.facebook.com')


# driver.page_source

# Opens facebook's source html file
soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.prettify())



# close webdriver object
driver.close()



