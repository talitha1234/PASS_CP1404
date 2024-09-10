"""
Activity 1 - User class
●	Write a User class, for a fun Taco Reward program
●	A User knows: name, number of tacos (starts at 5, goes down when they give a taco), and their score goes up by 1
●	A User can give a taco away to get a point
●	We should be able to print a User like:
        Ben, 2 points, 4 tacos left
●	When we make a user, they start with the name we want and appropriate default values

"""


class User:


if __name__ == '__main__':
    # this code will create the example output from slides
    chloe = User("Chloe")
    print(chloe)
    for i in range(6):
        chloe.give_taco()
    print(chloe)