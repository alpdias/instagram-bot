# -*- coding: utf-8 -*-

'''
Created in 07/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os
from pyfiglet import Figlet

# print text in ascii art
f = Figlet(font='slant')
instagramName = f.renderText('Instagram bot')

print(instagramName)
