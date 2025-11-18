# Create a class Car that uses this magic methods.
# def __init__() -> to set the brand and year data.
#  def __str__() -> to give a description of the car.

# This is just to show the understanding of the magic methods and how to create classes and instantiate objects.

class Car:
    def __init__(self , brand , year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"A {self.year} {self.brand} is a nice car."
    
# instantiate an object

car_1 = Car("Mercedes" , 2018)
print(car_1)

    
