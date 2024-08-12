"""PASS Revision Exercises."""

"""
1. Write a function that takes a list of numbers as a parameter and calculates and returns the average.
If the list is empty, it should catch a ZeroDivisionError, display an error message, and return None.
"""

def calculate_list_average(numbers_list):
    # start coding here

"""
2. Write a program that asks the user for a sentence and opens a file named 'words.txt'.
The program should write the sentence to the file with each word on a new line. (Remember to close the file!)
"""

def main1():
    # start coding here

"""
3. Write a function that takes a string as a parameter and returns True if it contains 5 or more vowels, otherwise it returns False.
"""

def five_vowels_check(text):
    # start coding here

"""
4. Write a program that asks the user for their name and has error checking to make sure it's not blank.
Then print every second letter in the name.
"""

def main2():
    # start coding here

"""
5. Write a function that takes a list of integers as a parameter and returns a new list containing only the numbers that are divisible by 3. Use a list comprehension.
"""

def get_divisible_by_three(numbers_list):
    # start coding here

"""
6. Write a function that takes a names-to-ages dictionary as a parameter, and an integer as a second parameter.
The function should return a new dictionary that contains only the key:value pairs if their age is larger than the
integer parameter.
"""

def get_older_people(names_to_ages, min_age):
    # start coding here

def get_older_people_comprehension(names_to_ages, min_age):
    # start coding here

"""
7. Write a function that takes a filename as an input parameter. It should open and read the file of comma-separated
 numbers, and return the sum of the values.
"""

def sum_file_numbers(filename):
    # start coding here

"""
8. Write a program that asks the user for their age and converts it to an integer. If an invalid input is received,
it should catch a ValueError, display an error message, and re-prompt the user until a valid input is received.
"""

def get_valid_age():
    # start coding here

"""
9. Write a function that takes a dictionary of items-to-prices and opens a file called 'item_prices.txt'.
The program should write the items to the file using string formatting as shown below.
items_to_prices = {"Milk" : 2.5, "Bread" : 3, "Aluminium Foil" : 5.45}

Milk                 $2.50
Bread                $3.00
Aluminium Foil       $5.45
"""

def print_items_to_prices(items_to_prices):
    # start coding here

"""
10. Write a function that takes a list of strings as a parameter and returns a new list containing only the strings
that end in a question mark. Use a list comprehension.
"""

def ends_in_question_mark(string_list):
    # start coding here

"""
11. Write a function that takes a names-to-ages dictionary as a parameter and returns a list of names that are in order
from youngest to oldest.
"""

def youngest_to_oldest(names_to_ages):
    # start coding here

def test_functions():
    # test each function in pycharm by calling them, make sure to use print when necessary as most only return a value
    # print(calculate_list_average([2, 8]))
    # main1()
    # print(five_vowels_check("aeioo"))
    # main2()
    # print(get_divisible_by_three([0, 3, 6, 8, 9]))
    # print(get_older_people({"Chloe": 19, "Bobbie": 7}, 8))
    # print(sum_file_numbers("revision.csv"))
    # get_valid_age()
    # print_items_to_prices({"Milk": 2.5, "Bread": 3, "Aluminium Foil": 5.45})
    # print(ends_in_question_mark(["question", "question mark?", "??", "?.."]))
    print(youngest_to_oldest({"Bob": 40, "Jerry": 50, "Frank": 35}))

test_functions()
