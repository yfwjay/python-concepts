from menu import *
from operations import *

def main():
    while True:
        menu()
        option = user_input()
        if option == "1":
            return addition()
        elif option == "2":
            return subtraction()
        elif option == "3":
            return division()
        elif option == "4":
            return multiplication()
        elif option == "5":
            return is_even()
        elif option == "6":
            return is_odd()
        elif option == "7":
            return exit_application()
            break
        elif option >= "8":
            print("Enter a valid option")
            return main()
        else:
            break
        
main()