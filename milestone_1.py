from tkinter import W

from pyparsing import Word


import random

word_list = ['apple', 'banana', 'watermelon', 'orange', 'grapefruit']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Enter a letter: ')
print('Letter:', guess)

if len(guess)==1 and guess.isalpha():
    print('Good Guess!')
else:
    print('Oops! That is not a valid input.')