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

    def __init__(self, name='', number_of_tacos=5, score=0.0):
        """Initialize a user with a name, number of tacos, and score."""
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __str__(self):
        """Returns string of user's name, score and number of tacos"""
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."

    def give_taco(self):
        """Give a taco and get a point."""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            self.score += 1
            print(f"{self.name} gave away one taco and now has {self.score} points.")
        else:
            print(f"{self.name} has no more tacos to give away")


if __name__ == '__main__':
    # this code will create the example output from above
    # Print a  user
    chloe = User("Chloe")

    # Give away a bunch of tacos
    print(chloe)
    for i in range(6):
        chloe.give_taco()
    print(chloe)

