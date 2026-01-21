
# Exercise 1
import numpy as np


def palindrome(word):
    word = word.replace(" ", "").lower()
    
    #Check if the string is the same forwards and backwards
    return word == word[::-1]

word = input("Enter a word or phrase: ")

if palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


# Exercise 2
import numpy as np


def parentheses(sequence):
    count =0
    
    for char in sequence:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        if count < 0:
            return False
        
    return count == 0

