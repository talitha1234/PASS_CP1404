import random

FILENAME = "numbers.txt"
RANDOM_MAX = 10
RANDOM_MIN = 1

# Get number in file
with open(FILENAME, 'r') as in_file:
    number_in_file = int(in_file.read())
print("Number in file", number_in_file)

# Write random number to file if greater than number in file
number = random.randint(1, 10)
print("Random number", number)
if number > number_in_file:
    with open(FILENAME, 'w') as out_file:
        print(number, file=out_file)



# number = random.randint(1, 10)
# if number < MAXIMUM:
#     with open(FILENAME, 'w') as out_file:
#         print(number, file=out_file)