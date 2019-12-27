# -*- coding: utf-8 -*-
'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# input info for bot 
print('')
username = input(str('User: '))
password = input(str('Password: '))
hashtag = input(str('Hashtag: '))
print('')
print('Loading...')
print('')
driver = webdriver.Firefox(executable_path=r'add here way to geckodriver.exe') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

# function to access the login page and log in
def botlogin (user, pwd):
    username = user # your user
    password = pwd # your password
    driver.get('https://www.instagram.com/') # instagram url
    sleep(1)
    loginbutton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']") # 'connect' button element
    loginbutton.click() # click on the 'connect' button
    sleep(1)
    userelement = driver.find_element_by_xpath("//input[@name='username']") # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element
    pwdelement = driver.find_element_by_xpath("//input[@name='password']") # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    sleep(2)


def loadpages(hashtag):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url
    sleep(2)
    for i in range(1, 6): # number of pages to load
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # scroll down to upload images
        i = i + 1
    print(f'Hashtag: {hashtag}')
    print(f'Pages: {i}')


botlogin(username, password)
loadpages(hashtag)
print('')

'''
# references html

# //a[@href='/accounts/login/?source=auth_switcher'] --> 'connect' button element
# //input[@name='username'] --> 'username' input element
# //input[@name='password'] --> 'password 'input element
'''
