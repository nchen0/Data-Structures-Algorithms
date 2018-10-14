"""
Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number. Assume you have 9 numbers between 1 to 10 and only one number is missing.

Example:
input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3
"""

# My Answer:


def find_missing_number(list_numbers):
    complete_list = [x for x in range(1, len(list_numbers) + 2)]
    for number in complete_list:
        if number not in list_numbers:
            return number

# Top Answer:


def find_missing_number(list_numbers):
    return sum(list(range(1, 11))) - sum(list_numbers)
