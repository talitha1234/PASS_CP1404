"""Space invaders game - PASS"""
import random

from boss import Boss
from invader import Invader

MENU = "a)ttack, e)nemies, q)uit"


def main():
    """The Space Invader program consists of a menu with 3 options.
   Attack - choose an enemy to attack
   Enemies - display all the enemies
   Quit - Quit the program
   HINT: Make a list of aliens to store the invader and boss objects
   HINT: Remember to remove the alien from the list once it's defeated!
   """
    aliens = [Invader(alien_type="Squid", health="100", color="yellow"),
              Invader(alien_type="Octopus", health="50", color="red"),
              Invader(alien_type="Crab", health="25", color="purple")]
    print("Welcome to Space Invaders!")
    print("Current enemies:")
    print_aliens(aliens)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "a":
            alien_index = int(input("Choose Alien (number): "))
            damage = random.randint(0, 100)
            aliens[alien_index].attack(damage)
            if aliens[alien_index].health <= 0:
                aliens.remove(aliens[alien_index])

        elif choice == "e":
            print_aliens(aliens)

        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ")
    print("Thanks for playing Space Invaders.")


def print_aliens(aliens):
    """Print all the aliens in the list on a new line, each with their list index in the form of:
   {list_index} - {alien_type}
   If all enemies have been defeated, output: 'All enemies have been defeated'"""
    for i, alien in enumerate(aliens):
        print(f"{i} - {alien.alien_type}")


def choose_alien(aliens):  # OPTIONAL
    """Choose an alien from the list of aliens with error checking.
   If the user choice is greater than the amount of aliens in the list output: 'Invalid (too high)'
   If the user choice is less than 0, output: 'Invalid (must be greater than 0)'
   If the user choice is not an integer, output: 'Invalid (not an integer)'"""
    # start coding here


main()
