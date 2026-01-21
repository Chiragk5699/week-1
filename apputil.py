# Exercise 1 

import numpy as np


def palindrome(s) :
    '''
    Given a word, return True if the word is a palindrome
    Flase Otherwise
    '''

    s = s.lower()
    return s == s[::-1]


# Exercise 2

def parentheses_checker(s):
    '''
    Given a string, return True if the string is balanced
    False Otherwise
    '''

    stack = []

    opening = set('({[')
    closing = set(')}]')

    matches = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return not stack

    