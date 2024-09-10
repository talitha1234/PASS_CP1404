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
            new_contact = get_contact()
            contacts.append(new_contact)
        elif choice == 'D':
            # TODO: Remove pass and add code to delete contact
            pass

        else:
            print("Invalid choice.")
        print()
        choice = input(MENU).upper()
    print("Goodbye :)")


def display_contacts(contacts):
    """Receives list of contacts as an input and prints each one on a new line using string formatting"""
    # Billy Bob : 0438236777
    # TODO: Add code to display contacts
    for contact in contacts:
        print(contact)


def get_contact():
    """Asks the user for input for the new contact's name and number. Returns the new contact as a tuple"""
    new_contact = ()
    # TODO: Add code to get contact
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    new_contact = (name, number)
    return new_contact


def get_valid_contact(contacts):
    """Asks the user for a first name to remove.
    If there is more than one person with the same first name, ask the user for a surname.
    If the name does not exist, display an error message. Returns the contact to remove as a tuple"""

    contact_to_remove = (input("Which contact would you like to remove? "))
    while contact_to_remove not in contacts:
        print("Contact not found.")
    if contact_to_remove in contacts:

    #     How to check for a unique contact name..

    # TODO: Add code to remove contact
    return contact_to_remove


main()
