# -*- coding: utf-8 -*-

'''
Created in 07/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from time import sleep
from pyfiglet import Figlet

def artName(timeSleep=0):
    
    """
    -> function to print text in ascii art\
    \n:param timeSleep: art loading time\
    \n:return: ascii art\
    """
    
    f = Figlet(font='slant')
    instagramName = f.renderText('Instagram bot')
    print(instagramName)
    sleep(timeSleep)

