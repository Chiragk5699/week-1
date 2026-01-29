# Exercise 1
def palindrome(word):
    """
    Check whether a given string is a palindrome.

    Parameters
    ----------
    word : str
        Input string to check.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.
    """
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]


# Exercise 2
def parentheses(sequence):
    """
    Check whether a string of parentheses is balanced.

    Parameters
    ----------
    sequence : str
        A string containing '(' and ')'.

    Returns
    -------
    bool
        True if parentheses are balanced, False otherwise.
    """
    count = 0

    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

        # Early failure if closing parenthesis appears first
        if count < 0:
            return False

    return count == 0

