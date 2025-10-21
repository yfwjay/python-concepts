age = int(input("Enter your age: "))
is_id =(input("Do you have your ID? ")).strip().lower()
time = int(input("Enter the time of the show in 24 hr format = "))


if age >= 18:
    print("Viable to book the ticket")
elif age < 18 and is_id == "yes" and time < 18:
    print("Just made it !! Viable to book the ticket")
else:
    print("Sorry you can't be able to book for a ticket")
