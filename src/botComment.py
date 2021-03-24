# -*- coding: utf-8 -*-

'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
import art
import random
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def functionComment(mySystem):
    
    """
    -> function for commenting photos\
    \n:param mySystem: operating system type\
    \n:return: bot to comment photos\
    """

    # check the system
    if mySystem == 'Linux': 
        mySystem = 'clear'
        way = Path('geckodriver/linux/geckodriver-v0.26.0-linux64') # path to the file
        geckoFile = way / 'geckodriver' # way to geckodriver

    else:
        mySystem = 'cls'
        way = Path('geckodriver/windows')
        geckoFile = way / 'geckodriver.exe' 

    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem)
    art.artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot
    os.system(mySystem) 
    art.artName(0)
    
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
        print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')


    def botlogin (user, pwd):
        
        """
        -> log in to instagram along with credentials\
        \n:param user: user to login\
        \n:param pwd: login password\
        \n:return: user's instagram login\
        """
        
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


    def findhashtag(hashtag):
        
        """
        -> function hashtag search page\
        \n:param hashtag: hashtag name\
        \n:return: hastag page\
        """

        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


    def typephrase(comment, field):
        
        """
        -> function to type letter by letter\
        \n:param comment: comment to be typed\
        \n:param field: field in which the comment will be inserted\
        \n:return: comment being written in the selected field in a more natural way\
        """

        for letter in comment: # commentary and lyrics
            
            field.send_keys(letter) # type the letter in the field
            sleep(0.09) # input time of each letter


    def likecomment(likes=1, comment=''):
        
        """
        -> function to like and comment the photos\
        \n:param likes: amount of likes\
        \n:param comment: comment on photo\
        \n:return: like and comment on photos\
        """ 

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
    try:
        botlogin(username, password)
        
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        
    except:
        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # executing function search hastag
    try:
        findhashtag(hashtag)
        
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        
    except:
        print('\033[0;31mUNEXPECTED ERROR ON HASHTAG PAGE\033[m, please try again and verify your connection!')

    # executing function to enjoy and comment
    try:
        likecomment(likes, comment)
        
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        
    except:
        print('\033[0;31mUNEXPECTED ERROR ON COMMENT\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 

