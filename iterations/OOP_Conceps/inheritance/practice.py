# Inheritance is a sub-class inheriting data and behaviour from another class.

# A Sub-class will be inheriting data and behaviour from a super-class.

class Person:
    # create a dunder method __init__
    def __init__(self , name , age):
        self.name = name
        self.age = age

    # create a method walk

    def walk(self):
        print(f"{self.name} is walking!!")
                

# create a subclass student that will inherit from Person

class Student(Person):
    # create only a method status 
    def status(self):
        print(f"{self.name} of {self.age} is a graduate!!")

# instantiate an object

student_1 = Student("James" , 20)

student_1.status()
student_1.walk()

# example 2

class Animal:
    def __init__(self , species):
        self.species = species

    def sound(self):
        print(f"The {self.species} makes a sound")

# create a suclass dog

class Dog(Animal):
    def bark(self):
        print(f"The {self.species} barks woof woof!!")

        # instantiate an object

dog_1 = Dog("Dog")

dog_1.bark()

