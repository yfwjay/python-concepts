import os
# Perform various Os functions such as'

# 1. METHOD getcwd()

# This method is used to get the current working directory we are working on.

working_directory = os.getcwd()
print("Current working directory is : " , working_directory)

# displays the current working directory.

# 2. METHOD mkdir()

# parent_directory = r"C:\python-concepts\iterations\Os_module"
# new_directory = "notes" # name of the directory you want to create

# # Join the 2 paths
# join_directory = os.path.join(parent_directory , new_directory)

# # Now create the directory

# make_directory = os.mkdir(join_directory)  # creates a new directory called notes at that specific location

# 3.METHOD chdir()

# This method is for changing the current working directory

# 4. METHOD lisdir()

# The method lists out the files present in a specific directory

directory_location = r"C:\python-concepts\iterations\Os_module"

# check the files present in that directory

files_present = os.listdir(directory_location)
print("FILES PRESENT" , files_present) # displays only the files present ion that specific directory


#  5. METHOD remove() 
# This method removes the path of an existing file

# Create a file james.txt. And try to delete it

# delete_file = os.remove(r"C:\python-concepts\iterations\Os_module\james.txt")

# present_file = os.listdir(r"C:\python-concepts\iterations\Os_module")
# print("FILES PRESENT" , present_file) # receive an error that the file james.txt is missing


# 6. METHOD rmdir()

# Deletes a present directory

temp_directory = "Temp_dir"
main_directory = "C:\python-concepts\iterations\Os_module"

join_two = os.path.join(main_directory , temp_directory)
# create_temp = os.mkdir(join_two) # create a temp directory at that location

delete_temp = os.rmdir(join_two)


