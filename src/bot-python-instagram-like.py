# -*- coding: utf-8 -*-
'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

# input info for bot 
os.system('cls')
print('')
print('\033[0;32mLOGIN INFORMATION\033[m')
print('')
username = str(input('User: ')) # your user
password = str(input('Password: ')) # your password
os.system('cls')
print('')
print('\033[0;32mBOT INFORMATION\033[m')
print('')
hashtag = str(input('Hashtag: ')) # hashtag
likes = int(input('Amount: ')) # amount of photos to like
print('')
print('Loading...')
print('')

# load browser drive in to var and open
try:
    driver = webdriver.Firefox(executable_path=r'add here way to geckodriver.exe') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
except:
    print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')

# function to access the login page and log in
def botlogin (user, pwd):
    username = user # your user
    password = pwd # your password
    driver.get('https://www.instagram.com/') # instagram url

    '''
    this page / button was removed by Instagram

    sleep(1)
    driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
    '''
    
    sleep(2)
    userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element
    pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    sleep(4)


# function hashtag search page
def findhashtag(hashtag):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


# function to like the photos
def like(likes=1):
    driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
    item = 1
    while item <= likes: # loop with how many photos to like
        try:
            sleep(2)
            driver.find_element_by_class_name('fr66n').click() # click the like button
            sleep(random.randint(40, 70)) # break time between likes and comment due to instagram policy against bots
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
            item = item + 1
        except:
            sleep(60) # if connection errors occur
    print(f'Number of photos liked: \033[0;33m{item - 1}\033[m')
    
    
# execution of functions
try:
    botlogin(username, password)
except KeyboardInterrupt:
    print('\033[0;33mProgram terminated by the user!\033[m')
except:
    print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')
try:
    findhashtag(hashtag)
except KeyboardInterrupt:
    print('\033[0;33mProgram terminated by the user!\033[m')
except:
    print('\033[0;31mUNEXPECTED ERROR ON HASHTAG PAGE\033[m, please try again and verify your connection!')
try:
    like(likes)
except KeyboardInterrupt:
    print('\033[0;33mProgram terminated by the user!\033[m')
except:
    print('\033[0;31mUNEXPECTED ERROR ON LIKE\033[m, please try again and verify your connection!')
print('')
print('Finish!')
print('')

'''
# references html
# //a[@href="/accounts/login/?source=auth_switcher"] --> 'connect' page button element
# //input[@name="username"] --> 'username' input element
# //input[@name="password"] --> 'password 'input element
# @class="v1Nh3" --> open photo
# @class="fr66n" --> like button
# @class="coreSpriteRightPaginationArrow" --> next photo button
'''
