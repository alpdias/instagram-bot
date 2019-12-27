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
hashtag = str(input('Hashtag: ')) # hashtag
likes = int(input('Amount: ')) # amount of photos to like
yourcomment = str(input('Comment: ')) # your comment on photos
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
    loginbutton = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
    userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element
    pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    sleep(2)


# function hashtag search page
def findhashtag(hashtag):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


# function to type letter by letter
def typephrase(comment, field):
    for letter in comment: # commentary and lyrics
        field.send_keys(letter) # type the letter in the field
        sleep(0.09) # input time of each letter

       
# function to like the photos
def likecomment(likes, yourcomment):
    driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
    item = 1 
    while item <= likes: # loop with how many photos to like
        sleep(1)
        driver.find_element_by_class_name('fr66n').click() # click the like button
        driver.find_element_by_class_name('Ypffh').click() # click the field to insert comment
        comment = driver.find_element_by_class_name('Ypffh')
        comment.clear()
        typephrase(yourcomment, comment) # insert comment typing each letter
        sleep(1)
        # the 'publish' button name changes according to your instagram language
        postcomment = driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click() # click the post 'comment' button element
        sleep(20) # break time between likes and comment due to instagram policy against bots
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
        item = item + 1


# execution of functions
botlogin(username, password)
findhashtag(hashtag)
likecomment(likes, yourcomment)

'''
# references html
# //a[@href='/accounts/login/?source=auth_switcher'] --> 'connect' page button element
# //input[@name='username'] --> 'username' input element
# //input[@name='password'] --> 'password 'input element
# @class='v1Nh3' --> open photo
# @class='fr66n' --> like button
# @class='coreSpriteRightPaginationArrow' --> next photo button
# @class='Ypffh' --> field to insert comment
# //button[contains(text(), "Publicar")] --> post 'comment' button element
'''
