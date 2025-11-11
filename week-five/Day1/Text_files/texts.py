# We will try to read and write files of .txt

# to write a file

# This creates a file names.txt using the method open that takes in 2 arguments.
# The name of the file you want to create and the mode eg write mode(w)
with open("names.txt" , "w") as file:
    name_1 = file.write("James \n")
    name_2 = file.write("Joy \n")
    name_3 = file.write("Ann \n")


# This creates a file names.txt with the names James , Joy , and Ann


# We now read the content in names.txt

with open("names.txt" , "r") as file:
    content = file.read()
    print(content)

# It will print the names present.