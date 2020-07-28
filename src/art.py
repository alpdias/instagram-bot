# -*- coding: utf-8 -*-

'''
Created in 07/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from pyfiglet import Figlet

# function to print text in ascii art
def art():
    f = Figlet(font='cricket')
    instagramName = f.renderText('Instagram bot')
    
    return instagramName

