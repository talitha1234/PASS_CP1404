"""PASS Revision Exercises."""

"""
1. Write a function that takes a list of numbers as a parameter and calculates and returns the average.
If the list is empty, it should catch a ZeroDivisionError, display an error message and return None.
"""


def calculate_list_average(numbers_list):
    try:
        return sum(numbers_list) / len(numbers_list)
    except ZeroDivisionError:
        print("Error: empty list")
        return None


"""
2. Write a program that asks the user for a sentence and opens a file named 'words.txt'.
The program should write the sentence to the file with each word on a new line. (Remember to close the file!)
"""


def main1():
    out_file = open("words.txt", 'w')
    user_sentence = input("Sentence: ")
    for word in user_sentence.split():  # the split method returns a list, it does not modify user_sentence directly
        print(word, file=out_file)
    out_file.close()  # close is a method, not a function


"""3. Write a function that takes a string as a parameter and returns True if it contains 5 or more vowels, 
otherwise it returns False."""


def five_vowels_check(text):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for vowel in text.lower():  # make sure to account for case sensitivity
        if vowel in vowels:
            count += 1
    return count >= 5  # you do not need to write an if statement, the expression already returns True or False


"""" 4. Write a program that asks the user for their name and has error checking to make sure it's not blank. Then 
print every second letter in the name."""


def main2():
    name = input("Name: ")
    while name == "":
        print("Name cannot be blank")
        name = input("Name: ")
    # for i in range(0, len(name) - 1, 2):  # prints using the range function
    #     print(name[i], end="")
    for c in (name[::2]):  # prints using slicing
        print(c, end="")


"""" 5. Write a function that takes a list of integers as a parameter and returns a new list containing only the 
numbers that are divisible by 3. Use a list comprehension."""


def get_divisible_by_three(numbers_list):
    return [number for number in numbers_list if number % 3 == 0]


"""6. Write a function that takes a names-to-ages dictionary as a parameter, and an integer as a second parameter. 
The function should return a new dictionary that contains only the key:value pairs if their age is larger than the 
integer parameter."""


def get_older_people(names_to_ages, min_age):
    older_names_to_ages = {}
    for name in names_to_ages:
        if names_to_ages[name] > min_age:
            older_names_to_ages[name] = names_to_ages[name]
    return older_names_to_ages


def get_older_people_comprehension(names_to_ages, min_age):
    return {name: age for name, age in names_to_ages.items() if
            age > min_age}  # Same as above but with a dictionary comprehension! Nice!


"""7. Write a function that takes a filename as an input parameter. It should open and read the file of comma 
separated numbers, and return the sum of the values."""


def sum_file_numbers(filename):
    in_file = open(filename)
    numbers = [int(number) for number in in_file.read().split(",")]  # great use of a list comprehension here
    return sum(numbers)


"""8.  Write a program that asks the user for their age and converts it to an integer. If an invalid input is 
received, it should catch a ValueError, display an error message, and re-prompt the user until a valid input is 
received."""


def get_valid_age():
    is_valid_input = False
    while not is_valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    print("Next year you will be", age + 1)


"""9.  Write a function that takes a dictionary of items-to-prices and opens a file called 'item_prices.txt'.
The program should write the items to the file using string formatting as shown below.
items_to_prices = {"Milk" : 2.5, "Bread" : 3, "Aluminium Foil" : 5.45}

Milk                 $2.50
Bread                $3.00
Aluminium Foil       $5.45
"""


def print_items_to_prices(items_to_prices):
    with open("item_prices.txt", "w") as out_file:
        for item, price in items_to_prices.items():
            print(f"{item}  ${price:.2f}", end="\n", file=out_file)


"""
10.    Write a function that takes a list of strings as a parameter and returns a new list containing only the strings 
that end in a question mark. Use a list comprehension.
"""


def ends_in_question_mark(string_list):
    new_list = []
    # long way vs list comprehension
    # for string in string_list:
    #     if string[-1] == "?":
    #         new_list.append(string)
    new_list = [string for string in string_list if string[-1] == "?"]
    return new_list


"""11.    Write a function that takes a names-to-ages dictionary as a parameter and returns a list of names that are 
in order from youngest to oldest."""


def youngest_to_oldest(names_to_ages):
    import operator
    return sorted(names_to_ages.items(), key=operator.itemgetter(1))


def test_functions():
    # test each function by calling them, make sure to use print when necessary as most only return a value
    print(calculate_list_average([2, 8]))
    main1()
    print(five_vowels_check("aeioo"))
    main2()
    print(get_divisible_by_three([0, 3, 6, 8, 9]))
    print(get_older_people({"Chloe": 19, "Bobbie": 7}, 8))
    print(sum_file_numbers("revision.csv"))
    get_valid_age()
    print_items_to_prices({"Milk": 2.5, "Bread": 3, "Aluminium Foil": 5.45})
    print(ends_in_question_mark(["question", "question mark?", "??", "?.."]))
    print(youngest_to_oldest({"Bob": 40, "jerry": 50, "frank": 35}))


test_functions()
