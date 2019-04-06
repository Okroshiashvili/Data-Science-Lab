"""
Created on Sat Apr  6 2019

@author: Nodar Okroshiashvili
"""




from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()

# open instagram.com
driver.get('https://www.instagram.com')

sleep(5)

# Finds log in button
login_button = driver.find_element_by_link_text('Log in')

# clicks log in button
login_button.click()


sleep(5)


driver.close()


