"""
Activity 1 - User class
Same as before except now user chooses another user to give a taco to
A User can give a taco away to another user to get a point, other user's points don't change
"""



class User:
    def __init__(self, name="", number_of_tacos=5, score=0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def give_taco(self, other):
        """Give away a taco."""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            self.score += 1

            print(f"{self.name} gave away away 1 taco and now has {self.score} points.")
            other.receive_taco()
        else:
            print(f"{self.name} has no more tacos to give away.")

    def receive_taco(self):
        """Receive a taco."""
        self.number_of_tacos += 1
        print(f"{self.name} got one taco and now has {self.number_of_tacos} tacos.")

    # def __str__(self):
    #     return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."

    def __repr__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."


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

    # ADD CODE HERE to print each user on a new line
    # do the for loop first
    print("Using for loop:")
    for user in users:
        print(user)

    # ADD CODE HERE list comprehension

    print("Using list comprehension:")
    # print([type(user) for user in users])
    print("\n".join(str(user) for user in users if user.name == ""))
