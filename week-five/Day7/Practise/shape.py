class Shape:
    def __init__(self , name , color):
        self.__name = name # a private data
        self.__color = color # a private data member
    def __str__(self):
        return(f"This is a {self.__name} of color {self.__color}")

class Rectangle(Shape):
    def __init__(self, name, color , length , width):
        super().__init__(name, color) # The parent constructor 

        self.length = length # Add extra data length
        self.width = width # Add extra data width

    def calculateArea(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, color , diameter , pi):
        super().__init__(name, color) # The parent constructor 

        self.diameter = diameter # Add extra data diameter
        self.pi = pi # Add extra data width

    def calculateCircumference(self):
        return self.diameter * self.pi


# we now create instances of the classes circle and rectangle

rectangle = Rectangle("Rectangle" , "Red" , 20 , 10)
circle = Circle("Circle" , "Blue" , 7 , 3.142)

print(rectangle)
print(circle)

print(f"The Area of the Rectangle of length {rectangle.length} and width {rectangle.width} is = {rectangle.calculateArea()}")

print(f"The Circumference of the Circle of Diameter {circle.diameter} is = {circle.calculateCircumference()}")
    
"""
The code Above demonstrates the understanding of the following concepts:

1.Instantiate Classes. 
-> Able to design a class shape
2.Use of Dunder methods str and init
3.Inheritance
-> Have created a Parent class (shape) and sub-classes (rectangle and circle)
4.Encapsualtion
-> In the parent class we have made the data (name and color) to be private by adding a prefix (__) double underscores
5. Instantiating Objects
"""