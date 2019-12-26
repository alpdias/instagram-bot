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
driver = webdriver.Firefox(executable_path=r'add here way to geckdriver.exe') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
botlogin(username, password)
likephoto(hashtag)
print('')

# function to access the login page and log in
def botlogin (user, pwd):
    username = user # your user
    password = pwd # your password
    driver.get('https://www.instagram.com/') # instagram url
    sleep(2)
    loginbutton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']") # 'connect' button element
    loginbutton.click() # click on the 'connect' button
    sleep(2)
    userelement = driver.find_element_by_xpath("//input[@name='username']") # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element
    pwdelement = driver.find_element_by_xpath("//input[@name='password']") # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    sleep(4)


def likephoto(hashtag):
    driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/') # instagram tag page url
    sleep(4)
    for i in range(1, 3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # scroll down to upload images
        i = i + 1
        sleep(4)
    hrefs = driver.find_elements_by_tag_name('a') # get the photo links
    hrefsphotos = [elem.get_attribute('href') for elem in hrefs]
    [href for href in hrefsphotos if hashtag in href]
    print(f'Hashtag: {hashtag}')
    print(f'Photos: {str(len(hrefsphotos))}')
    print(f'Pages: {i}')
    for hrefsphotos in hrefsphotos:
        driver.get(hrefsphotos) 
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # scroll down to upload images
        try:
            driver.find_elements_by_class_name('//button[@class="dCJp8 afkep"]').click() # click the like button
            sleep(20)
        except:
            sleep(10)

'''
# references html

# //a[@href='/accounts/login/?source=auth_switcher'] --> 'connect' button element
# //input[@name='username'] --> 'username' input element
# //input[@name='password'] --> 'password 'input element

'''
