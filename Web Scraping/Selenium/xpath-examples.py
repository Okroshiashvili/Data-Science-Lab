from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('/Users/waqarjoyia/Downloads/chromedriver')

# instagram example

'''
driver.get('https://www.instagram.com')

sleep(2)
login_button = driver.find_element_by_xpath("//span[@id='react-root']//p[@class='_dyp7q']/a") # valid

login_button.click()

sleep(5)

'''
# google example

driver.get('https://www.google.com')
sleep(2)

searchbar = driver.find_element_by_xpath("//input[@id='lst-ib']")       #

searchbar.send_keys('valid xpath expression')

searchbar.submit()

sleep(5)

driver.close()