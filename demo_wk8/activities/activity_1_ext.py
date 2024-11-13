"""
Activity 1 - User class
Same as before except now user chooses another user to give a taco to
A User can give a taco away to another user to get a point, other user's points don't change
Compare the score of 2 users using overloading operators.
"""



# Add your code from activity one and add to it.


if __name__ == '__main__':
    # EXTENSION - Output is in the slide
    chloe = User("Chloe")
    tim = User("Tim")
    dorothy = User("dorothy")
    # other_users = [tim, dorothy]
    print(chloe)
    for i in range(6):
        chloe.give_taco([tim, dorothy])
    print(chloe)
    users = [chloe, tim]
    print("As list: ")
    print(users)

    #TODO - add code here to print each user on a new line
    # do the for loop first
    print("Using for loop:")

    #TODO - list comprehension
    # needs to convert to string because user in this context without the str then user is returned as User object
    # and join expects a list of strings
    print("Using list comprehension:")


    #TODO - Compare users


