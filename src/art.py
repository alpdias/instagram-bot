# -*- coding: utf-8 -*-

'''
Created in 07/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from time import sleep
from pyfiglet import Figlet

# function to print text in ascii art
def artName(timeSleep=0):
    f = Figlet(font='slant')
    instagramName = f.renderText('Instagram bot')
    
    print(instagramName)
    sleep(timeSleep)

