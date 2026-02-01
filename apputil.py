# Exercise 1 

import numpy as np


def palindrome(s):
    '''
    Given a word or phrase, return True if it is a palindrome.
    False otherwise.
    Ignores case, spaces, and punctuation.
    '''
    
    # Convert to lowercase
    s = s.lower()
    
    # Keep only alphanumeric characters (letters and numbers)
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char
    
    # Check if cleaned string is a palindrome
    return cleaned == cleaned[::-1]


s = input("Enter a word or phrase: ")

if palindrome(s):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


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

    