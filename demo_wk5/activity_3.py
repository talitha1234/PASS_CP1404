"""
Activity 2 - Contacts Program. Complete each of the functions by following their instructions.
See below for an example output. Blue is for user input.

Menu:


"""

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

            contact_to_delete = get_valid_contact(contacts)

            # length will be either 0 for an empty tuple or 3 for a tuple with contact details
            if len(contact_to_delete) != 0:
                contacts.remove(contact_to_delete)
                print(f'{contact_to_delete[0]} has been removed')

        else:
            print("Invalid choice.")
        print()
        choice = input(MENU).upper()
    print("Goodbye :)")


def display_contacts(contacts):
    # for contact in contacts:
    #     print(f'{contact[0]} {contact[1]}: {contact[2]}')
    contacts_to_display = '\n'.join([f"{contact[0]} {contact[1]}: {contact[2]}" for contact in contacts])
    print(contacts_to_display)

def get_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")
    new_contact = (first_name, last_name, phone_number)
    return new_contact


def get_valid_contact(contacts):
    # Get list of contacts with this first name
    first_name = input("Who would you like to remove (first name): ")
    contacts_with_first_name = []
    contact_to_remove = ()
    for contact in contacts:
        if contact[0] == first_name:
            contacts_with_first_name.append(contact)

    # If more than one contact with first name then ask for last name
    if len(contacts_with_first_name) > 1:
        print(f"Found multiple entries with the first name {first_name}")
        last_name = input("Who would you like to remove? (last name): ")

        for contact in contacts:
            if contact[1] == last_name:
                contact_to_remove = contact

    # If there's only one contact with that first name then set contact to remove as this contact
    elif len(contacts_with_first_name) == 1:
        for contact in contacts:
            if first_name in contact:
                return contact
    else:
        print(f'Could not find {first_name}')

    return contact_to_remove


main()
