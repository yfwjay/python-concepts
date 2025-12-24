# We'll try to create classes and instantiate objects


# We can create a class person with the following attributes:
# 1. Name 2. Age 3. Gender

class Person:
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    # We create a method walk

    def walk(self):
        walk = (f"{self.name} of age {self.age} is a {self.gender} and is walking!! ")
        return walk


# instantiate an object

name_input = input("Enter your name = ")
age_input = input("Enter your Age = ")
gender_input = input("Enter your Gender = ")

student = Person(name_input ,age_input, gender_input)

print(student.walk())



# Practise dunder method __str__

class Car:
    def __init__(self , brand , year):
        self.brand = brand
        self.year = year
    
    # Define a dunder method str
    # Dunder method str is for giving a description so that when we instantiate an object it immediately executes

    def __str__(self):
        return(f"{self.brand} of year {self.year} is moving!!")
            
    # instantiate an object

car_1 = Car("Mercedes" , 2018)

print(car_1)