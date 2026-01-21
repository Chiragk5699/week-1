


import numpy as np


def palindrome(s) :
    '''
    Given a word, return True if the word is a palindrome
    Flase Otherwise
    '''

    s = s.lower()


    return s == s[::-1]

s = input ("Enter a word or Phrase")

if palindrome(s):
    print ("It is a palindrome")
else:
    print ("It is not a palidrome")



