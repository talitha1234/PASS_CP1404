"""
Activity 1 - User class
Same as before except now user chooses another user to give a taco to
A User can give a taco away to another user to get a point, other user's points don't change
"""


class User:
    """Return a string representation of a user."""
    def __init__(self, name='', number_of_tacos=5, score=0.0):
        """Initialize a user with a name, number of tacos, and score."""
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __repr__(self):
        """Returns string of user's name, score and number of tacos"""
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."

    def give_taco(self, other_users):
        """Give a taco and get a point, other user gets a taco."""
        """Give a taco away and get a point."""
        if self.number_of_tacos > 0:
            self.score += 1
            self.number_of_tacos -= 1
            print(f"{self.name} gave away one taco and now has {self.score} points")
        else:
            print(f"{self.name} has no more tacos to give away")


if __name__ == '__main__':
    # EXTENSION
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

    # add code here to print each user on a new line
    # do the for loop first
    print("Using for loop:")
    for user in users:
        print(user)

    # list comprehension
    # needs to convert to string because user in this context without the str then user is returned as User object
    # and join expects a list of strings
    print("Using list comprehension:")
    print("\n".join(str(user) for user in users))
