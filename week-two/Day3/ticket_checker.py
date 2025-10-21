# Ask the user to enter their age

age = int(input("Enter your age: "))

if age > 18 :
    print("You are qualified to watch R-rated movies")
elif age == 18 :
    print("Just made it!! But carry ID just in case.")
else:
    print("You are under-age")