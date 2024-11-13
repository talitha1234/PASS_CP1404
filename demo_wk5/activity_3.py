"""
Activity 3 - Contacts Program. Complete each of the functions by following their instructions.
See below for an example output. Blue is for user input.

Menu:


"""

from operator import itemgetter

MENU = """V)iew
A)dd
D)elete
Q)uit
>>> """


def main():
    """Menu program of contacts."""
    contacts = [("Billy", "Bob", "0438236777"), ("Kate", "Murphey", "04983266322"),
                ("Daniel", "Peterson", "0478872633"), ("Billy", "Jones", "0456321856")]

    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'V':
            display_contacts(contacts)
        elif choice == 'A':
            new_contact = get_new_contact()
            contacts.append(new_contact)
        elif choice == 'D':
            # TODO: Remove pass and add code to delete contact
            pass
        else:
            pass
        print()
        choice = input(MENU).upper()
    print("Goodbye :)")


def display_contacts(contacts):
    """Receives list of contacts as an input and prints each one on a new line using string formatting"""
    # TODO: Add code to display contacts (formatted like in word doc)
    for contact in contacts:
        print(contact)


def get_new_contact():
    """Asks the user for input for the new contact's name and number. Returns the new contact as a tuple"""
    # TODO: Add code to get contact (first name, last name and number)


def get_valid_contact(contacts):
    """Asks the user for a first name to remove.
    If there is more than one person with the same first name, ask the user for a surname.
    If the name does not exist, display an error message. Returns the contact to remove as a tuple"""

    first_name = input("Who would you like to remove? (first name): ")
    for contact in contacts:
        if contact[0] == first_name:
            return contact[0]


def get_contact_to_remove(contacts):
    """Asks the user for a first name to remove.
    #TODO: If there is more than one person with the same first name, ask the user for a surname.
    #TODO: If the name does not exist, display an error message. Returns the contact to remove as a tuple"""
    first_name = input("Who would you like to remove? (first name): ")
    for contact in contacts:
        if contact[0] == first_name:
            return contact


main()
