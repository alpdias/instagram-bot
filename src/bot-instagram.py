# -*- coding: utf-8 -*-

'''
Created in 07/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
import art
import botLike
import botComment
import botStories

while True:
    
    art.artName(2)

    menu = ['Like', 'Comment and Like', 'View Stories']

    for indice, lista in enumerate(menu): # loop to generate an index in the list of options
        print(f'\033[0;34m[{indice}]\033[m {lista}') # print the list of options

    print('')
    selected = int(input('Select a function for the bot: ')) # receive the function that will be started
    print('')

    if selected == 0:
        botLike.functionLike() # bot to like

    elif selected == 1:
        botComment.functionComment() # bot to like and comment

    elif selected == 2:
        botStories.functionStories() # bot to see stories

    else:
      print('Option invalid, please try again!')
