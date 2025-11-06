# This is where we define each function like each users option what it does

contacts = []




contacts_set = set()
contacts_set = set()

def add_contact():
    global contacts_set
    # User prompted to enter the contact name and phone_number
    con_name = input("Enter the contact name = ").strip().title()
    con_num = input("Enter the phone number = ")

    # we need to store each entry of the contact in dictionary
    # we define the dictionary
    contact_book = {
        "Name" : con_name , 
        "Phone_Number" : con_num
    }

    # Now we append each entry of our contact to the list contacts

    contacts.append(contact_book)

    # We print a message telling the user we have successfuly added the contact

    print(f"Contact {con_name} added successfuly")

    # To make sure there are no duplicates we define aset where we will be adding our contacts
    contacts_set.add(con_name)


def view_contacts():
    # We define the functionality of seeing the contacts present

    # Remember our contacts are in a list so we must loop through our list

    # we 1st check if the contacts are present
    if len(contacts) == 0:
        print("No contacts Present")
        return
    print("------ALL CONTACTS---------")
    # we now iterate through our contact list using a for loop
    for indx , contact_book in enumerate(contacts , start = 1):
        print(f"{indx} . {contact_book['Name']} -> {contact_book['Phone_Number']}")


def search_contact():
    search_value = input("Enter Name or Phone Number: ").strip().lower()

    found = False

    for contact in contacts:
        # Convert both sides to lowercase for case-insensitive matching
        name_lower = contact["Name"].lower()
        number_lower = contact["Phone_Number"].lower()

        # Partial match for name OR exact or partial match for number
        if search_value in name_lower or search_value in number_lower:
            print(f"Found: {contact['Name']} - {contact['Phone_Number']}")
            found = True

    if not found:
        print("Contact not found.")




def exit_application():
    print("You have exited the application")