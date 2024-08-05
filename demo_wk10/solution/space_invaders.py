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
   HINT: Create a list of aliens that contains the Invader and Boss type aliens and choose their respective arguments.
"""
    aliens = [Invader("Squid", 10, "White"), Invader("Squid lvl 2", 20, "Black"),
              Boss("Octopus", 20, 40)]
    print("Welcome to Space Invaders!")
    print("Current enemies:")
    print_aliens(aliens)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "a":
            current_alien = choose_alien(aliens)
            damage = random.randint(0, 50)
            current_alien.attack(damage)
            if current_alien.health < 0:
                aliens.remove(current_alien)
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
    if len(aliens) > 0:
        for i, alien in enumerate(aliens):
            print(f"{i} - {alien}")
    else:
        print("All enemies have been defeated!")


def choose_alien(aliens):
    """Choose an alien from the list of aliens with error checking.
   If the user choice is greater than the amount of aliens in the list output: 'Invalid (too high)'
   If the user choice is less than 0, output: 'Invalid (must be greater than 0)'
   If the user choice is not an integer, output: 'Invalid (not an integer)'"""
    is_valid_input = False
    while not is_valid_input:
        try:
            choice = int(input("Choose alien (number): "))
            if choice < 0:
                print("Invalid (must be greater than 0)")
            elif choice > len(aliens) - 1:
                print("Invalid (too high)")
            else:
                return aliens[choice]
        except ValueError:
            print("Invalid (not an integer)")


main()
