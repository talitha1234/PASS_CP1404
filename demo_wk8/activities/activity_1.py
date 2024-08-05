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
    def __init__(self, name="", number_of_tacos=5, score=0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score


    def give_taco(self):
        """Give away a taco."""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            self.score += 1
            print(f"{self.name} has given away 1 taco. {self.number_of_tacos} tacos remaining.")
        else:
            print(f"{self.name} has no remaining tacos")


    def __str__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."


if __name__ == '__main__':
    # this code will create the example output from slides
    chloe = User("Chloe")
    print(chloe)
    for i in range(6):
        chloe.give_taco()
    print(chloe)