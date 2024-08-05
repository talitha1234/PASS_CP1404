"""
Solution to class task
Note there are many ways to solve this problem, this is just one solution.
Have a play with using .read(), .readline() and .readlines() - and become familiar with what they will return!
"""

is_file_valid = False
while not is_file_valid:
    try:
        filename = input("Filename: ")
        in_file = open(filename)  # default mode to open is read ('r')
        is_file_valid = True
    except FileNotFoundError:
        print("Please enter a valid file")

word_to_find = input("Word to find: ")
count = 0

for line in in_file:  # the for loop implicitly reads a line at a time - you don't use .read() or .readline() methods
    words = line.split()  # splits the line of text around whitespace and returns an array of words
    for word in words:
        if word.lower() == word_to_find.lower():  # using lower means that the user input is not case sensitive
            count += 1
print("The word {} appears in the file {} {} times".format(word_to_find, filename, count))
in_file.close()  # ALWAYS CLOSE YOUR FILES WHEN YOU ARE FINISHED

# Different ways to read:
# print(in_file.readline())
# print(in_file.readlines())
# print(in_file.read())
