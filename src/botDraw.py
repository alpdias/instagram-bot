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

def functionDraw(mySystem):

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
    art.artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mBOT INFORMATION\033[m')
    print('')
    imgPage = str(input('URL Image: ')) # photo path on instagram
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:
        driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    except:
        try:
            driver = webdriver.Firefox(executable_path=f'{geckoFile}')
        except:
            print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')


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


    # function img search page
    def findImg(imgPage):

        driver.get(f'{imgPage}') # instagram img page url
        
        
    # running function for login
    try:
        botlogin(username, password)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # executing function search img
    try:
        findImg(imgPage)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON IMG PAGE\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')
    
    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 
