class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} of age {self.age} is walking!!")

# We create a student class

class Student(Person):
    def status(self):
        print(f"{self.name} is a graduate!!")

# Instantiate an object

student = Student("James" , 20)

student.walk()
student.status()

