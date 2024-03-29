# Unique Chars in a String: https://www.firecode.io/pages/explore/288821
"""
Write a function that takes in an input string and returns True if all the characters in the string are unique, False if there is even a single repeated character.

Examples:
 
unique_chars_in_string("abcde") -> True

unique_chars_in_string("aa") -> False

unique_chars_in_string("") -> True
"""


def unique_chars_in_string(input_string):
    x = set(input_string)
    print('x is: ', x)
    print(len(x))
    print('input_string is: ', input_string)
    print(len(input_string))
    if len(x) == len(input_string):
        return True
    else:
        return False

# Alternative:


def unique_chars_in_string(input_string):
    return len(set(input_string)) == len(input_string)
