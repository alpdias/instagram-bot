# -*- coding: utf-8 -*-

'''
Created in 10/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
import platform
from time import sleep
from pyfiglet import Figlet
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# function to print text in ascii art
def artName(timeSleep=0):
    f = Figlet(font='slant')
    instagramName = f.renderText('Instagram bot')
    
    print(instagramName)
    sleep(timeSleep)


def functionLike(mySystem):

    # check the system
    if mySystem == 'Linux': 
        mySystem = 'clear'
        way = Path('geckodriver/linux/geckodriver-v0.26.0-linux64') # path to the file
        geckoFile = way / 'geckodriver' # way to geckodriver

    else:
        mySystem = 'cls'
        way = Path('geckodriver/windows') # path to the file
        geckoFile = way / 'geckodriver.exe' # way to geckodriver

    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
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
        driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    except:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}')

    # function to access the login page and log in
    def botlogin (user, pwd):

        username = user # your user
        password = pwd # your password
        
        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
        '''
        
        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(delay + 2)


    # function hashtag search page
    def findhashtag(hashtag):

        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


    # function to like the photos
    def like(likes=1):

        driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload

        item = 1

        while item <= likes: # loop with how many photos to like

            try:
                sleep(delay)
                driver.find_element_by_class_name('fr66n').click() # click the like button
                sleep(random.randint(40, 70)) # break time between likes and comment due to instagram policy against bots
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
                item = item + 1
                
            except:
                sleep(60) # if connection errors occur

        print(f'Number of photos liked: \033[0;33m{item - 1}\033[m')
        
        
    # running function for login
    botlogin(username, password)

    # executing function search hastag
    findhashtag(hashtag)

    # executing function to enjoy
    like(likes)

    print('')
    print('Finish!')
    print('')
    
    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 
    
    
def functionComment(mySystem):

    # check the system
    if mySystem == 'Linux': 
        mySystem = 'clear'
        way = Path('geckodriver/linux/geckodriver-v0.26.0-linux64') # path to the file
        geckoFile = way / 'geckodriver' # way to geckodriver

    else:
        mySystem = 'cls'
        way = Path('geckodriver/windows') # path to the file
        geckoFile = way / 'geckodriver.exe' # way to geckodriver

    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mBOT INFORMATION\033[m')
    print('')
    hashtag = str(input('Hashtag: ')) # hashtag
    likes = int(input('Amount: ')) # amount of photos to like
    comment = str(input('Comment: ')) # comment in photos
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    except:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}')

    # function to access the login page and log in
    def botlogin (user, pwd):
        
        username = user # your user
        password = pwd # your password

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
        '''
        
        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(delay + 2)


    # function hashtag search page
    def findhashtag(hashtag):

        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


    # function to type letter by letter
    def typephrase(comment, field):

        for letter in comment: # commentary and lyrics
            field.send_keys(letter) # type the letter in the field
            sleep(0.09) # input time of each letter


    # function to like the photos
    def likecomment(likes=1, comment=''):

        driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
        
        item = 1

        while item <= likes: # loop with how many photos to like
            
            try:
                sleep(delay)
                driver.find_element_by_class_name('fr66n').click() # click the like button
                driver.find_element_by_class_name('Ypffh').click() # click the field to insert comment
                field = driver.find_element_by_class_name('Ypffh')
                field.clear()
                typephrase(comment, field) # insert comment typing each letter
                sleep(delay)

                # the 'publish' button name changes according to your instagram language
                driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click() # click the post 'comment' button element
                sleep(random.randint(380, 420)) # break time between likes and comment due to instagram policy against bots
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
                item = item + 1

            except:
                sleep(60) # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')

    # running function for login
    botlogin(username, password)

    # executing function search hastag
    findhashtag(hashtag)

    # executing function to enjoy and comment
    likecomment(likes, comment)

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 


def functionStories(mySystem):

    # check the system
    if mySystem == 'Linux': 
        mySystem = 'clear'
        way = Path('geckodriver/linux/geckodriver-v0.26.0-linux64') # path to the file
        geckoFile = way / 'geckodriver' # way to geckodriver

    else:
        mySystem = 'cls'
        way = Path('geckodriver/windows') # path to the file
        geckoFile = way / 'geckodriver.exe' # way to geckodriver

    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    delay = int(input('Delay (just number): ')) # loading delay time

    # input info for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    artName(0)
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    except:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}')

    # function to access the login page and log in
    def botlogin (user, pwd):

        username = user # your user
        password = pwd # your password

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button 
        '''
        
        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(4)


    # function to view the stories
    def stories():

        try:
            driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)
            
        except:
            pass

        try:
            driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click() # press the notification button that appears most of the time, denying the option
            sleep(delay)
            
        except:
            pass

        driver.find_element_by_class_name('_6q-tv').click() # click on the tab where the stories are
        sleep(delay)

        loadstories = '' # variable to terminate the loop without errors

        while loadstories != 0:

            sleep(delay)

            try:
                driver.find_element_by_class_name('coreSpriteRightChevron').click() # next storie button
                
            except KeyboardInterrupt:
                print('\033[0;33mProgram terminated by the user!\033[m')
                loadstories = 0
                
            except:
                print('\033[0;33mEND! No more stories to view\033[m') 
                loadstories = 0


    # running function for login
    botlogin(username, password)
 
    # running function to see the stories
    stories()

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 

mySystem = platform.system() # which operating system is running

while True:
    
    artName(2)

    menu = ['Like', 'Comment and Like', 'View Stories']

    for indice, lista in enumerate(menu): # loop to generate an index in the list of options
        print(f'\033[0;34m[{indice}]\033[m {lista}') # print the list of options

    print('')
    print('\033[0;33m(to finish press Ctrl + C)\033[m')
    selected = int(input('Select a function for the bot: ')) # receive the function that will be started
    print('')

    if selected == 0:
        functionLike(mySystem) # bot to like

    elif selected == 1:
        functionComment(mySystem) # bot to like and comment

    elif selected == 2:
        functionStories(mySystem) # bot to see stories

    else:
      print('Option invalid, please try again!')
