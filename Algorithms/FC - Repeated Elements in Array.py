"""
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]
"""

# My answer:


def duplicate_items(list_numbers):
    list_numbers.sort()
    arr = []
    temp = None
    for number in list_numbers:
        if number == temp:
            arr.append(number)
        temp = number
    return arr

# Top answer:


def duplicate_items(list_numbers):
    set_list = set(list_numbers)
    return [i for i in set_list if list_numbers.count(i) > 1]
