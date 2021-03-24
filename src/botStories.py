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

def functionStories(mySystem):
    
    """
    -> function to see stories\
    \n:param mySystem: operating system type\
    \n:return: bot to see stories\
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

    # input info for bot 
    os.system(mySystem)
    art.artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    os.system(mySystem)
    art.artName(0)
    
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


    def stories():
        
        """
        -> function to view the stories\
        \n:return: see stories on instagram\
        """

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
    try:
        botlogin(username, password)
        
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        
    except:
        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # running function to see the stories
    try:
        stories()
        
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        
    except:
        print('\033[0;31mUNEXPECTED ERROR ON STORIES\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 

