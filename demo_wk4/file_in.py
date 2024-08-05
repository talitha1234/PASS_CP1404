"""
CP1404 - Wk4 demo - Reading files
"""

FILE_NAME = "bank-data.csv"

file_in = open(FILE_NAME, 'r')
thing_1 = file_in.readline()
"""What is the output of thing_1?"""
print(thing_1)

"""What is the output of thing_2?"""
thing_2 = file_in.read()
print(thing_2)
# file_in.close()


"""What is the output of thing_3 if the file is still open?"""
thing_3 = file_in.readlines()
print("Start")
print(thing_3)
print("End")
# file_in.close()


"""What will readlines print?"""
file_in.seek(0)
thing_3 = file_in.readlines()
print("Readlines")
print(thing_3)
print()

"""What about read?"""
file_in.seek(0)
thing_3 = file_in.read()
print("Read")
print(thing_3)
file_in.close()