contacts = {}

def add_phone():
    global contacts
    name = input("Enter Your name: \n").lower()
    # contacts["Name"] = name

    number = input("Enter The Phone Number: \n")
    # contacts["Number"] = number

    contacts[name] = number

    print(f"Added {name} to the phone Book")

def view_contacts():
    global contacts
    if len(contacts) == 0 :
        print("You have no Contacts in your Phone book")
    else:
        for key , value in contacts.items():
            print(f"{key} -> {value}")

def exit_application():
    print("You have successfuly exited the application!!")
