# We define the functionality of our system.

from tasks import *
from menu import *


def main():
        menu()
        user_choice()
        while True:
            choice = user_choice()
            if choice == "1":
                set_budget()
            elif choice == "2":
                add_items()
            elif choice == "3":
                view_items()
            elif choice == "4":
                remove_item()
            elif choice == "5":
                total_budget()
            elif choice == "6":
                exit_application()
                break
            else:
                print("Enter a Valid choice.")

main()