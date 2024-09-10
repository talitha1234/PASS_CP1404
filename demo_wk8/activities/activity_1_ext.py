"""
Activity 1 - User class
Same as before except now user chooses another user to give a taco to
A User can give a taco away to another user to get a point, other user's points don't change
"""



class User:



if __name__ == '__main__':
    # EXTENSION
    chloe = User("Chloe")
    tim = User("Tim")
    print(chloe)
    for i in range(6):
        chloe.give_taco(tim)
    print(chloe)
    users = [chloe, tim]
    print("As list: ")
    print(users)

    # print each user on a new line
    # do the for loop first

    print("Using list comprehension:")
    # ADD CODE HERE list comprehension



