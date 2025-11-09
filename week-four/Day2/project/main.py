from menu import *
from tasks import *

def main():
    while True:
        menu()
        choice = get_user_input()
        if choice == "1":
             add_phone()
        elif choice == "2":
             view_contacts()
        elif choice == "3":
             exit_application()
             break
        else:
            print("Enter a Valid choice between (1-3)")

main()


