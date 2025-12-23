# This creates a file known as details.txt 

# with open takes 2 paramteres name of the file and the mode = write mode
# Just specify what you want to write in the file

with open("details.txt" , "w") as file:
    name_1 = file.write("\n James")
    name_2 = file.write("\n Joy")
    name_3 = file.write("\n Joan")


# We know use read mode to read what is in our file

with open("details.txt" , "r") as file:
    content = file.read()

    print(content)

with open("details.txt" , "a" ) as file:
    name_3 = file.write("\n John")

with open("details.txt" , "r") as file:
    content = file.readlines()
    # print(content)

    # for indx , i in enumerate(content , start = 1):
    #     print(f'{indx}.{i.strip()}')

