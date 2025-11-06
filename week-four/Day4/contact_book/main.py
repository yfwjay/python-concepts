# Here we define the functionality of our phone book

# we 1st import the necessary modules

from menu import *
from tasks import *

# We then define our main function

def main():
    while True:
        contact_menu()
        choice = user_choice()
        # choice = user_choice()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            exit_application()
            break
        else:
            print("Invalid choice.Try again")

main()
