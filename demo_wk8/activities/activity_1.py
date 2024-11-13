"""
Activity 1 - User class
●	Write a User class, for a fun Taco Reward program
●	A User knows: name, number of tacos (starts at 5, goes down when they give a taco), and their score
●	A User can give a taco away to get a point
●	We should be able to print a User like:
        Chloe, 2 points, 4 tacos left
●	When we make a user, they start with the name we want and appropriate default values

"""


class User:
    """Return a string representation of a user."""

    def __init__(self):
        """Initialize a user with a name, number of tacos, and score."""



    def give_taco(self):
        """Give a taco and get a point."""



if __name__ == '__main__':
    # this code will create the example output from above
    # Print a  user
    chloe = User("Chloe")

    # Give away a bunch of tacos
    print(chloe)
    for i in range(6):
        chloe.give_taco()
    print(chloe)


"""
Explanation on main block:
The __main__ block is used to ensure that certain code is only executed when the script is run directly,
 and not when it is imported as a module in another script. 
"""


# print("in class file activity 1 __name__ = ", __name__)
