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

def artName(timeSleep=0):
    
    """
    -> function to print text in ascii art\
    \n:param timeSleep: waiting time for execution\
    \n:return: ascii art\
    """
    
    f = Figlet(font='slant')
    instagramName = f.renderText('Instagram bot')
    print(instagramName)
    sleep(timeSleep)


def functionLike(mySystem):
    
    """
    -> function to enjoy photos\
    \n:param mySystem: operating system type\
    \n:return: bot to enjoy photos\
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
    artName(0)
    
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) 
    artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot 
    os.system(mySystem)
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
    driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
  
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


    def like(likes=1):
        
        """
        -> function to like the photos\
        \n:param likes: amount of likes\
        \n:return: enjoy the photos\
        """

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
    artName(0)
    
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) 
    artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot
    os.system(mySystem)
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
    driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

    
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
    artName(0)
    
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    
    delay = int(input('Delay (just number): ')) # loading delay time

    # input info for bot 
    os.system(mySystem) 
    artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    os.system(mySystem) 
    artName(0)
    
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
    
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


def functionDraw(mySystem):
    
    """
    -> function to comment several times on photos of draw\
    \n:param mySystem: operating system type\
    \n:return: bot to comment several times on sweepstakes photos\
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
    artName(0)
    
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem)
    artName(0)
    
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot 
    os.system(mySystem)
    artName(0)
    
    print('')
    print('\033[0;32mBOT INFORMATION\033[m')
    print('')
    
    imgPage = str(input('URL Image: ')) # photo path on instagram
    amount = int(input('Number of Comments: ')) # number of comments
    comment = str(input('Comment: ')) # comment
    
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    driver = webdriver.Firefox(executable_path=f'{geckoFile}') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

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


    def findImg(imgPage):
        
        """
        -> function hashtag search page\
        \n:param imgPage: image page\
        \n:return: selected page\
        """

        driver.get(f'{imgPage}') # instagram img page url

        
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


    def commentDraw(amount=1, comment=''):
        
        """
        -> function to comment on the draw photo\
        \n:param amount: number of comments\
        \n:param comment: comment on photo\
        \n:return: comment on several photos\
        """
        
        driver.find_element_by_class_name('fr66n').click() # click the like button

        item = 1
        
        while item <= amount: # 
            
            try:
                sleep(delay)
                driver.find_element_by_class_name('Ypffh').click() # click the field to insert comment
                field = driver.find_element_by_class_name('Ypffh')
                field.clear()
                typephrase(comment, field) # insert comment typing each letter
                sleep(delay)

                # the 'publish' button name changes according to your instagram language

                driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click() # click the post 'comment' button element
                sleep(random.randint(15, 30)) # break time between likes and comment due to instagram policy against bots
                item = item + 1

            except: 
                sleep(60) # if connection errors occur

        print(f'Number of commented: \033[0;33m{item - 1}\033[m')

    
    # running function for login
    botlogin(username, password)
        
    # running function for search img draw
    findImg(imgPage)

    # running function for draw comments
    commentDraw(amount, comment)

    print('')
    print('Finish!')
    print('')
    
    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 


mySystem = platform.system() # which operating system is running

while True:
    
    artName(2)
    
    menu = ['Like', 'Comment and Like', 'View Stories', 'Draw for Comment']

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
    
    elif selected == 3:
        functionDraw(mySystem) # bot to draw comments

    else:  
      print('Option invalid, please try again!')
