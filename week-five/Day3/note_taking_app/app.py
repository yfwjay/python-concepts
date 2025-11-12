# Create the functions that will be defining what the app will be doing.

def add_note():
    while True:
        try:
            note = input("Enter a note (or press Enter to stop): ").strip()
            if note == "":  # exit when user presses Enter without typing
                print("Exiting note adder.")
                break

            with open("your_notes.txt", "a") as file:
                file.write(note + "\n")  # write note without extra space
                print(f"Added -> {note}")
        except FileNotFoundError:
            print("File was not found!!")
            break  # stop if file can't be opened


def view_notes():
    # we want to see what is in the txt file your_notes.
    # we also know that this lists will be stored in a list
    # print our notes
    try:
        with open("your_notes.txt" , "r") as file:
            present_notes = file.readlines()
            if present_notes:
                print("==========YOUR NOTES========")
                for indx , notes in enumerate(present_notes , start= 1):
                    print(f"{indx}.{notes.strip()}")
            else:
                print("No notes in your file")
    except FileNotFoundError:
        print("Your file could not be found")

def delete_note():
    # we define the functionality for deleting a note
    view_notes()
    try:
        choice = int(input("Enter the note number to delete = "))
        with open("your_notes.txt" , "r")as file:
            notes = file.readlines()

            if 0 < choice <= len(notes):
                removed_notes = notes.pop(choice - 1)
                with open("your_notes.txt" , "w") as file:
                    file.writelines(notes)
                    print(f"Deleted: {removed_notes.strip()}")
            else:
                print("Invalid Note-number")
    except ValueError:
        print("Enter a valid Number")
    except FileNotFoundError:
        print("No notes found")


def main():
    print("Hello! Welcome to note taking app")

    while True:
        print("""
          1. Add a note
          2. View notes
          3. Delete a note
          4. Exit
        """)

        try:
            choice = int(input("Select an Option(1-4) = "))
        except ValueError:
            print("Please enter a valid number (1-4).")
            continue

        if choice == 1:
            add_note()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            delete_note()
        elif choice == 4:
            print("You have successfully exited the application.")
            break
        else:
            print("Enter a valid choice!!")


if __name__ == ("__main__"):
    main()