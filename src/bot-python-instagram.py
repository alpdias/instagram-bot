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
username = str(input('User: ')) # your user
password = str(input('Password: ')) # your password
hashtag = str(input('Hashtag to like: ')) # hashtag
likes = int(input('Amount of photos: ')) # amount of photos to like
print('')
print('Loading...')
print('')

# load browser drive in to var
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


# hashtag search function
def searchhashtag(hashtag):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


# function to like the photos
def likephoto(likes):
    driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
    items = 1 
    while items <= likes: # loop with how many photos to like
        sleep(2)
        driver.find_element_by_class_name('fr66n').click() # click the like button
        sleep(20)
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
        items = items + 1


# execution of functions
botlogin(username, password)
searchhashtag(hashtag)
likephoto(likes)
print('Finish!')
print('')

'''
# references html
# //a[@href='/accounts/login/?source=auth_switcher'] --> 'connect' button element
# //input[@name='username'] --> 'username' input element
# //input[@name='password'] --> 'password 'input element
# @class='v1Nh3' --> open photo
# @class='fr66n' --> like button
# @class='coreSpriteRightPaginationArrow' --> next photo button
'''
