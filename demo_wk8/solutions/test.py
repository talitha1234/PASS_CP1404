class User:
    """Return a string representation of a user."""
    def __init__(self, name='', number_of_tacos=5, score=0):
        """Initialize a user with a name, number of tacos, and score."""
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __repr__(self):
        """Returns string of user's name, score and number of tacos"""
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left."

    def give_taco(self, other_users):
        """Give a taco and get a point, other users get a taco."""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            self.score += 1
            for other_user in other_users:
                other_user.number_of_tacos += 1
                print(f"{self.name} gave one taco to {other_user.name}.")
            print(f"{self.name} now has {self.score} points and {self.number_of_tacos} tacos left.")
            for other_user in other_users:
                print(f"{other_user.name} now has {other_user.number_of_tacos} tacos.")
        else:
            print(f"{self.name} has no more tacos to give away.")


if __name__ == '__main__':
    # Create instances of User
    chloe = User("Chloe")
    tim = User("Tim")
    dorothy = User("Dorothy")

    # Example interaction
    print(chloe)  # Print initial status of Chloe
    chloe.give_taco([tim, dorothy])  # Chloe gives tacos to Tim and Dorothy
    print(chloe)  # Print updated status of Chloe

    # Display users as a list
    users = [chloe, tim, dorothy]
    print("\nAs list:")
    for user in users:
        print(user)
