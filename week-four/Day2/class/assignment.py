# Create a dictionary with the name student with the keys name , grade , and courses.

student = {
    "Name" : "John" ,
    "Grade" : "A" ,
    "Courses" : "BCOM"
}


# Then add a new key called graduated with a value of false
student["Graduate"] = False

print(student)



# An experiment of maybe taking input from the user they enter their name  , age  , Courses and whether graduated


# We initialize an empty dictionary
student_1 = {}

#We introduce the user to the questions

print("====================WELCOME==========================")

# name = input("Enter Your name: \n").lower()
# student_1["Name"] = name

# age = input("Enter Your Age: \n")
# student_1["Age"] = age

# Course = input("Enter Your Course: \n").upper()
# student_1["Course"] = Course

# Graduated = input("Have You Graduated?: \n").lower()
# student_1["Graduated"] = Graduated

# print("This are your Details: \n")

# for key , value in student_1.items():
#     print(f"{key} -> {value}")



# Issue with the above is that it overwrites thge previous student details
    

print("=============================================================")

students = []  # a list to hold all student dictionaries

def add_student():
    student_1 = {}
    student_1["Name"] = input("Enter your name: \n").lower()
    student_1["Age"] = input("Enter your age: \n")
    student_1["Course"] = input("Enter your course: \n").upper()
    student_1["Graduated"] = input("Have you graduated?: \n").lower()

    students.append(student_1)  #  add this student to the list
    print(f"\n{student_1['Name'].title()} added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("All Students:\n")
        for i, student in enumerate(students, start=1):
            print(f"Student {i}:")
            for key, value in student.items():
                print(f"  {key} -> {value}")
            print()

