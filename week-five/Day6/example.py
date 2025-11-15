# Create 2 classes a Parent class and a Sub-class.
# A parent class - Animal
# Sub-class -> Different types of animals we can have.

class Animal:
    def __init__(self , name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound!!")

# We create a sub-class and in here we pass our parent class as a parameter

class Dog(Animal):
    def barks(self):
        print(f"{self.name} is barking!!" )

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is Meowing!!")

# We instantiate an object

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.barks()
cat.meow()